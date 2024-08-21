from flask import Flask, jsonify, request, render_template
from sqlalchemy import create_engine, Column, Integer, String, text, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
import logging

# Flask app
app = Flask(__name__)

# Database connection details
DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@db/emumba_qor'

# Set up the database engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# SQLAlchemy Base
Base = declarative_base()

def parse_fermi_file(file_path):
    data = {}
    current_section = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('['):
                current_section = line.strip('[]')
                data[current_section] = []
            elif '=' in line:
                key, value = line.split('=', 1)
                data[current_section].append((key.strip(), value.strip()))
    return data


def create_table_class(table_name):
    attrs = {
        '__tablename__': table_name,
        'id': Column(Integer, primary_key=True, autoincrement=True),  # Primary key
        'properties': Column(String(255)),  # Column for keys
        'value': Column(String(255))  # Column for values
    }
    return type(table_name, (Base,), attrs)

def create_combined_table_class():
    attrs = {
        '__tablename__': 'All_Data',
        'id': Column(Integer, primary_key=True, autoincrement=True),  # Primary key
        'properties': Column(String(255)),  # Column for keys
        'value': Column(String(255))  # Column for values
    }
    return type('All_Data', (Base,), attrs)


def create_tables_from_log(data):
    inspector = inspect(engine)  # Create an inspector instance

    for section, entries in data.items():
        if not section.strip():  # Skip empty sections
            continue
        
        table_name = section.replace(' ', '_')
        # Create table class with id, properties, and value columns
        table_class = create_table_class(table_name)
        
        # Drop table if it already exists (for debugging purposes)
        if inspector.has_table(table_name):
            print(f"Dropping existing table: {table_name}")
            Base.metadata.drop_all(engine, tables=[table_class.__table__])
        
        Base.metadata.create_all(engine, tables=[table_class.__table__])
        
        # Verify table creation
        print(f"Created table: {table_name} with columns: {[c.name for c in table_class.__table__.columns]}")

    # Create the combined table
    combined_table_class = create_combined_table_class()
    if inspector.has_table('All_Data'):
        print(f"Dropping existing table: All_Data")
        Base.metadata.drop_all(engine, tables=[combined_table_class.__table__])
    
    Base.metadata.create_all(engine, tables=[combined_table_class.__table__])
    print(f"Created table: All_Data with columns: {[c.name for c in combined_table_class.__table__.columns]}")

def insert_data_to_tables(data):
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        for section, entries in data.items():
            table_name = section.replace(' ', '_')
            print(f"Inserting data into table: {table_name}")  # Debug print

            if table_name not in Base.metadata.tables:
                print(f"Table {table_name} does not exist in metadata")
                continue

            table = Base.metadata.tables[table_name]
            
            for key, value in entries:
                entry_dict = {
                    'properties': key,
                    'value': value
                }
                
                try:
                    stmt = insert(table).values(entry_dict)
                    session.execute(stmt)
                except Exception as e:
                    print(f"Error adding record to table {table_name}: {e}")
                    
            try:
                session.commit()
            except Exception as e:
                print(f"Error committing session for table {table_name}: {e}")
                session.rollback()

        # Insert data into the combined table
        combined_table = Base.metadata.tables['All_Data']
        
        for section, entries in data.items():
            for key, value in entries:
                entry_dict = {
                    'properties': key,
                    'value': value
                }
                try:
                    stmt = insert(combined_table).values(entry_dict)
                    session.execute(stmt)
                except Exception as e:
                    print(f"Error adding record to table All_Data: {e}")
                    
        try:
            session.commit()
        except Exception as e:
            print(f"Error committing session for All_Data: {e}")
            session.rollback()
    finally:
        session.close()

# Reusable function to execute queries
def execute_query(query, params=None):
    with engine.connect() as connection:
        result = connection.execute(text(query), params or {})
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result.fetchall()]
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    table_name = request.args.get('table_name')
    if not table_name:
        return render_template('error.html', message="Table name is required."), 400
    
    query = f'SELECT * FROM {table_name}'
    data = execute_query(query)
    if not data:
        return render_template('error.html', message=f"No data found for table '{table_name}'."), 404

    return render_template('results.html', data=data, table_name=table_name)


@app.route('/search_by_property', methods=['GET'])
def search_by_property():
    property_name = request.args.get('property_name')
    if not property_name:
        return render_template('error.html', message="Property name is required."), 400

    query = '''
        SELECT * FROM All_Data
        WHERE properties = :property_name
    '''
    data = execute_query(query, {'property_name': property_name})
    if not data:
        return render_template('error.html', message=f"No data found for property '{property_name}'."), 404

    return render_template('results.html', data=data, table_name='All_Data')



@app.route('/search_by_runs', methods=['GET'])
def search_by_runs():
    fermi_id = request.args.get('fermi_id')
    user = request.args.get('user')
    name = request.args.get('name')
    revision = request.args.get('revision')

    if not fermi_id and not user and not name and not revision:
        return render_template('error.html', message="Please enter at least one search criterion."), 400

    conditions = []
    params = {}

    if fermi_id:
        conditions.append("properties = 'fermi_id' AND value = :fermi_id")
        params['fermi_id'] = fermi_id
    if user:
        conditions.append("properties = 'user' AND value = :user")
        params['user'] = user
    if name:
        conditions.append("properties = 'name' AND value = :name")
        params['name'] = name
    if revision:
        conditions.append("properties = 'revision' AND value = :revision")
        params['revision'] = revision

    # Check for each individual condition
    for condition in conditions:
        check_query = f'''
            SELECT 1 FROM All_Data
            WHERE {condition}
        '''
        check_data = execute_query(check_query, params)
        if not check_data:
            return render_template('error.html', message="Data not found for the given criteria."), 404

    # If all conditions are valid, proceed with data retrieval
    query = '''
        SELECT * FROM All_Data
    '''
    data = execute_query(query)

    return render_template('results.html', data=data, table_name='All_Data')


@app.route('/<analysis_type>', methods=['GET'])
def get_analysis_data(analysis_type):
    valid_tables = {
        'geometric-analysis': 'Geometric_Analysis_Stats_Fermi',
        'main-stats': 'Main_Stats',
        'runtime-analysis': 'Runtime_Analysis_Stats',
        'statistical-analysis': 'Statistical_Analysis'
    }

    table_name = valid_tables.get(analysis_type)
    if not table_name:
        return "Invalid analysis type", 400

    query = f'SELECT * FROM {table_name}'
    data = execute_query(query)
    return render_template('results.html', data=data, table_name=analysis_type)
@app.route('/parse-and-insert', methods=['POST'])
def parse_and_insert():
    file_path = request.form.get('file_path', '../rsync/qor/fermi.txt')
    logging.info(f"Attempting to access file: {file_path}")
    try:
        data = parse_fermi_file(file_path)
        create_tables_from_log(data)
        insert_data_to_tables(data)
        return jsonify({"status": "Data parsed and inserted successfully"})
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)

