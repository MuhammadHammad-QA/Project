import sqlalchemy as db
from sqlalchemy import create_engine, Column, Integer, String, insert, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import inspect
import sys, os
#from sqlalchemy.ext.declarative import declarative_base

# Define the database URL
#DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor'
DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@db/emumba_qor'

# Use the correct import for declarative_base in SQLAlchemy 2.x
Base = declarative_base()

# Function to parse the fermi.txt file
def parse_fermi_file(file_path):
    data = {}
    current_section = None
    job_id = None

    # Read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('['):
                current_section = line.strip('[]')
                data[current_section] = []
            elif '=' in line:
                key, value = line.split('=', 1)
                if key.strip() == 'fermi_id':
                    job_id = value.strip()
                    data[current_section].append((key.strip(), value.strip()))
                else:
                    data[current_section].append((key.strip(), value.strip()))
    
    return data, job_id

def create_table_class(table_name):
    attrs = {
        '__tablename__': table_name,
        'id': Column(Integer, primary_key=True, autoincrement=True),  # Primary key
        'job_id': Column(String(255)),  # Column for job_id
        'properties': Column(String(255)),  # Column for keys
        'value': Column(String(255))  # Column for values
    }
    return type(table_name, (Base,), attrs)

def create_combined_table_class():
    attrs = {
        '__tablename__': 'All_Data',
        'id': Column(Integer, primary_key=True, autoincrement=True),  # Primary key
        'job_id': Column(String(255)),  # Column for job_id
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
        # Create table class with id, job_id, properties, and value columns
        table_class = create_table_class(table_name)
        
        # Create table if it does not exist
        if not inspector.has_table(table_name):
            print(f"Creating table: {table_name}")
            Base.metadata.create_all(engine, tables=[table_class.__table__])
        else:
            print(f"Table {table_name} already exists")

    # Create the combined table if it does not exist
    combined_table_class = create_combined_table_class()
    if not inspector.has_table('All_Data'):
        print(f"Creating table: All_Data")
        Base.metadata.create_all(engine, tables=[combined_table_class.__table__])
    else:
        print(f"Table All_Data already exists")


def insert_data_to_tables(data, job_id):
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
            
            # Check if job_id already exists
            existing_job = session.query(table).filter_by(job_id=job_id).first()
            
            for key, value in entries:
                entry_dict = {
                    'job_id': job_id,
                    'properties': key,
                    'value': value
                }
                
                if existing_job:
                    # Update existing records
                    try:
                        stmt = text(f"""
                            UPDATE {table_name}
                            SET value = :value
                            WHERE job_id = :job_id AND properties = :properties
                        """)
                        session.execute(stmt, entry_dict)
                    except Exception as e:
                        print(f"Error updating record in table {table_name}: {e}")
                else:
                    # Insert new records
                    try:
                        stmt = text(f"""
                            INSERT INTO {table_name} (job_id, properties, value)
                            VALUES (:job_id, :properties, :value)
                            ON DUPLICATE KEY UPDATE
                            value = VALUES(value)
                        """)
                        session.execute(stmt, entry_dict)
                    except Exception as e:
                        print(f"Error adding record to table {table_name}: {e}")
                    
            try:
                session.commit()
            except Exception as e:
                print(f"Error committing session for table {table_name}: {e}")
                session.rollback()

        # Insert or update data into the combined table
        combined_table = Base.metadata.tables['All_Data']
        
        existing_combined_job = session.query(combined_table).filter_by(job_id=job_id).first()
        
        for section, entries in data.items():
            for key, value in entries:
                entry_dict = {
                    'job_id': job_id,
                    'properties': key,
                    'value': value
                }
                
                if existing_combined_job:
                    
                    # Update existing records in the combined table
                    try:
                        stmt = text("""
                            UPDATE All_Data
                            SET value = :value
                            WHERE job_id = :job_id AND properties = :properties
                        """)
                        session.execute(stmt, entry_dict)
                    except Exception as e:
                        print(f"Error updating record in table All_Data: {e}")
                else:
                    # Insert new records into the combined table
                    try:
                        stmt = text("""
                            INSERT INTO All_Data (job_id, properties, value)
                            VALUES (:job_id, :properties, :value)
                            ON DUPLICATE KEY UPDATE
                            value = VALUES(value)
                        """)
                        session.execute(stmt, entry_dict)
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
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <file_path>")
        sys.exit(1)
    

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist or is not accessible.")
        sys.exit(1)

    # Parse the log file
    data, job_id = parse_fermi_file(file_path)

    # Set up the database engine
    engine = create_engine(DATABASE_URL)

    # Create tables
    create_tables_from_log(data)

    # Insert data
    insert_data_to_tables(data, job_id)



