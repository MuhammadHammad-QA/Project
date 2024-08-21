
from flask import Flask, jsonify, request, render_template
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Database connection details
DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor'

# Set up the database engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

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

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=7000)




# @app.route('/search_by_id', methods=['GET'])
# def search_by_id():
#     record_id = request.args.get('id')
#     if not record_id:
#         return "ID is required", 400
    
#     query = 'SELECT * FROM All_Data WHERE id = :id'
#     data = execute_query(query, {'id': record_id})
#     return render_template('results.html', data=data, table_name='All_Data')