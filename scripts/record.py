import sqlalchemy as db
from sqlalchemy import create_engine, Column, Integer, String, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

# Define the database URL
DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor'

# Use the correct import for declarative_base in SQLAlchemy 2.x
Base = db.orm.declarative_base()

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


if __name__ == '__main__':
    # Parse the log file
    file_path = '../11610/qor/fermi.txt'
    data = parse_fermi_file(file_path)

    # Set up the database engine
    engine = create_engine(DATABASE_URL)

    # Create tables
    create_tables_from_log(data)

    # Insert data
    insert_data_to_tables(data)
