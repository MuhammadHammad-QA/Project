# from flask import Flask, jsonify, request, render_template
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker

# app = Flask(__name__)

# # Database connection details
# DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor'

# # Set up the database engine and session
# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/geometric-analysis', methods=['GET'])
# def get_geometric_analysis():
#     query = text('SELECT * FROM Geometric_Analysis_Stats_Fermi')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return render_template('geometric_analysis.html', data=data)

# @app.route('/main-stats', methods=['GET'])
# def get_main_stats():
#     query = text('SELECT * FROM Main_Stats')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return render_template('main_stats.html', data=data)

# @app.route('/runtime-analysis', methods=['GET'])
# def get_runtime_analysis():
#     query = text('SELECT * FROM Runtime_Analysis_Stats')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return render_template('runtime_analysis.html', data=data)

# @app.route('/statistical-analysis', methods=['GET'])
# def get_statistical_analysis():
#     query = text('SELECT * FROM Statistical_Analysis')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return render_template('statistical_analysis.html', data=data)

# if __name__ == '__main__':
#     app.run(debug=True, host='localhost', port=7000)














# from flask import Flask, jsonify, request, render_template
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker

# app = Flask(__name__)

# # Database connection details
# DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor'

# # Set up the database engine and session
# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

# # Reusable function to execute queries
# def execute_query(query, params=None):
#     with engine.connect() as connection:
#         result = connection.execute(text(query), params or {})
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return data

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/search', methods=['GET'])
# def search():
#     table_name = request.args.get('table_name')
#     if not table_name:
#         return "Table name is required", 400
    
#     query = f'SELECT * FROM {table_name}'
#     data = execute_query(query)
#     return render_template('search_results.html', data=data, table_name=table_name)

# @app.route('/search_by_id', methods=['GET'])
# def search_by_id():
#     record_id = request.args.get('id')
#     if not record_id:
#         return "ID is required", 400
    
#     query = 'SELECT * FROM All_Data WHERE id = :id'
#     data = execute_query(query, {'id': record_id})
#     return render_template('search_results.html', data=data, table_name='All_Data')





# @app.route('/search_by_runs', methods=['GET'])
# def search_by_runs():
#     fermi_id = request.args.get('fermi_id')
#     if not fermi_id:
#         return "Fermi ID is required", 400

#     # Check if the Fermi ID exists in the table
#     check_query = '''
#         SELECT * FROM All_Data
#         WHERE properties = 'fermi_id' AND value = :fermi_id
#     '''
#     check_data = execute_query(check_query, {'fermi_id': fermi_id})

#     if not check_data:
#         return "Fermi ID not found", 404

#     # If Fermi ID exists, retrieve all data from All_Data
#     query = '''
#         SELECT * FROM All_Data
#     '''
#     data = execute_query(query)

#     return render_template('search_results.html', data=data, table_name='All_Data')



# @app.route('/<analysis_type>', methods=['GET'])
# def get_analysis_data(analysis_type):
#     valid_tables = {
#         'geometric-analysis': 'Geometric_Analysis_Stats_Fermi',
#         'main-stats': 'Main_Stats',
#         'runtime-analysis': 'Runtime_Analysis_Stats',
#         'statistical-analysis': 'Statistical_Analysis'
#     }

#     table_name = valid_tables.get(analysis_type)
#     if not table_name:
#         return "Invalid analysis type", 400

#     query = f'SELECT * FROM {table_name}'
#     data = execute_query(query)
#     return render_template(f'{analysis_type}.html', data=data)

# if __name__ == '__main__':
#     app.run(debug=True, host='localhost', port=7000)













































# from flask import Flask, jsonify, request, render_template
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker

# app = Flask(__name__)

# # Database connection details
# DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@db/emumba_qor'

# # Set up the database engine and session
# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/geometric-analysis', methods=['GET'])
# def get_geometric_analysis():
#     query = text('SELECT * FROM Geometric_Analysis_Stats_Fermi')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return render_template('geometric_analysis.html', data=data)

# @app.route('/main-stats', methods=['GET'])
# def get_main_stats():
#     query = text('SELECT * FROM Main_Stats')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return render_template('main_stats.html', data=data)

# @app.route('/runtime-analysis', methods=['GET'])
# def get_runtime_analysis():
#     query = text('SELECT * FROM Runtime_Analysis_Stats')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return render_template('runtime_analysis.html', data=data)

# @app.route('/statistical-analysis', methods=['GET'])
# def get_statistical_analysis():
#     query = text('SELECT * FROM Statistical_Analysis')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return render_template('statistical_analysis.html', data=data)

# if __name__ == '__main__':
#     app.run(debug=True)






























# from flask import Flask, jsonify, request
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker

# app = Flask(__name__)

# # Database connection details
# DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor'

# # Set up the database engine and session
# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

# @app.route('/')
# def index():
#     return "Welcome to the API!"


# @app.route('/geometric-analysis', methods=['GET'])
# def get_geometric_analysis():
#     query = text('SELECT * FROM Geometric_Analysis_Stats_Fermi')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return jsonify(data)

# @app.route('/main-stats', methods=['GET'])
# def get_main_stats():
#     query = text('SELECT * FROM Main_Stats')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return jsonify(data)

# @app.route('/runtime-analysis', methods=['GET'])
# def get_runtime_analysis():
#     query = text('SELECT * FROM Runtime_Analysis_Stats')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return jsonify(data)

# @app.route('/statistical-analysis', methods=['GET'])
# def get_statistical_analysis():
#     query = text('SELECT * FROM Statistical_Analysis')
#     with engine.connect() as connection:
#         result = connection.execute(query)
#         columns = result.keys()
#         data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return jsonify(data)


# # Add similar endpoints for other tables if needed, e.g., Main_Stats, Runtime_Analysis_Stats, Statistical_Analysis

# if __name__ == '__main__':
#     app.run(debug=True)















































# import sqlalchemy as db
# from sqlalchemy import create_engine, Column, Integer, String, insert
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import inspect  # Import inspect

# # Define the database URL
# DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor'

# # Use the correct import for declarative_base in SQLAlchemy 2.x
# Base = db.orm.declarative_base()

# def parse_fermi_file(file_path):
#     data = {}
#     current_section = None

#     with open(file_path, 'r') as file:
#         for line in file:
#             line = line.strip()
#             if not line or line.startswith('['):
#                 current_section = line.strip('[]')
#                 data[current_section] = []
#             elif '=' in line:
#                 key, value = line.split('=', 1)
#                 data[current_section].append((key.strip(), value.strip()))
#     return data

# def create_table_class(table_name):
#     attrs = {
#         '__tablename__': table_name,
#         'id': Column(Integer, primary_key=True, autoincrement=True),  # Primary key
#         'properties': Column(String(255)),  # Column for keys
#         'value': Column(String(255))  # Column for values
#     }
#     return type(table_name, (Base,), attrs)

# def create_tables_from_log(data):
#     inspector = inspect(engine)  # Create an inspector instance

#     for section, entries in data.items():
#         if not section.strip():  # Skip empty sections
#             continue
        
#         table_name = section.replace(' ', '_')
#         # Create table class with id, properties, and value columns
#         table_class = create_table_class(table_name)
        
#         # Check if the table already exists
#         if inspector.has_table(table_name):
#             print(f"Table {table_name} already exists. Skipping creation.")
#         else:
#             Base.metadata.create_all(engine, tables=[table_class.__table__])
#             # Verify table creation
#             print(f"Created table: {table_name} with columns: {[c.name for c in table_class.__table__.columns]}")

# def insert_data_to_tables(data):
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     try:
#         for section, entries in data.items():
#             table_name = section.replace(' ', '_')
#             print(f"Inserting data into table: {table_name}")  # Debug print

#             if table_name not in Base.metadata.tables:
#                 print(f"Table {table_name} does not exist in metadata")
#                 continue

#             table = Base.metadata.tables[table_name]
            
#             for key, value in entries:
#                 entry_dict = {
#                     'properties': key,
#                     'value': value
#                 }
                
#                 print(f"Processing entry: {entry_dict} (type: {type(entry_dict)})")  # Debug print
                
#                 try:
#                     stmt = insert(table).values(entry_dict)
#                     session.execute(stmt)
#                 except Exception as e:
#                     print(f"Error adding record to table {table_name}: {e}")
                    
#             try:
#                 session.commit()
#             except Exception as e:
#                 print(f"Error committing session for table {table_name}: {e}")
#                 session.rollback()
#     finally:
#         session.close()

# if __name__ == '__main__':
#     # Parse the log file
#     file_path = '../rsync/qor/fermi.txt'
#     data = parse_fermi_file(file_path)

#     # Set up the database engine
#     engine = create_engine(DATABASE_URL)

#     # Create tables
#     create_tables_from_log(data)

#     # Insert data
#     insert_data_to_tables(data)

















































# import re
# import sqlalchemy as db
# from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, DateTime, insert
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # Define the database URL
# DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor'

# # Use the correct import for declarative_base in SQLAlchemy 2.x
# Base = db.orm.declarative_base()

# def parse_fermi_file(file_path):
#     data = {}
#     current_section = None

#     with open(file_path, 'r') as file:
#         for line in file:
#             line = line.strip()
#             if not line or line.startswith('['):
#                 current_section = line.strip('[]')
#                 data[current_section] = []
#             elif '=' in line:
#                 key, value = line.split('=', 1)
#                 data[current_section].append((key.strip(), value.strip()))
#     return data

# def create_table_class(table_name, columns):
#     attrs = {
#         '__tablename__': table_name,
#         'id': Column(Integer, primary_key=True, autoincrement=True)  # Add an id column as primary key
#     }
#     for column_name, column_type in columns.items():
#         if column_type == 'Integer':
#             attrs[column_name] = Column(Integer)
#         elif column_type == 'Float':
#             attrs[column_name] = Column(Float)
#         elif column_type == 'String':
#             attrs[column_name] = Column(String(255))
#         elif column_type == 'Boolean':
#             attrs[column_name] = Column(Boolean)
#         elif column_type == 'DateTime':
#             attrs[column_name] = Column(DateTime)
#     return type(table_name, (Base,), attrs)

# def create_tables_from_log(data):
#     for section, entries in data.items():
#         if not section.strip():  # Skip empty sections
#             continue
        
#         table_name = section.replace(' ', '_')
#         columns = {}
        
#         for key, value in entries:
#             if ' ' in value:
#                 columns[key] = 'Float'
#             elif value.lower() in ['true', 'false']:
#                 columns[key] = 'Boolean'
#             elif re.match(r'\d+\.\d+', value):
#                 columns[key] = 'Float'
#             elif re.match(r'\d+', value):
#                 columns[key] = 'Integer'
#             else:
#                 columns[key] = 'String'


#         # Limit columns to the first 5
#         columns = dict(list(columns.items())[:5])
#         # print(f"Creating table: {table_name} with columns: {columns}")  # Debug print

#         table_class = create_table_class(table_name, columns)
#         Base.metadata.create_all(engine, tables=[table_class.__table__])

# def insert_data_to_tables(data):
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     try:
#         for section, entries in data.items():
#             table_name = section.replace(' ', '_')
#             print(f"Inserting data into table: {table_name}")  # Debug print

#             if table_name not in Base.metadata.tables:
#                 print(f"Table {table_name} does not exist in metadata")
#                 continue

#             table = Base.metadata.tables[table_name]
            
#             for entry in entries:
#                 # Convert the tuple to a dictionary
#                 # Assuming entry is a tuple of (key, value)
#                 entry_dict = dict([entry])
                
#                 print(f"Processing entry: {entry_dict} (type: {type(entry_dict)})")  # Debug print
                
#                 try:
#                     stmt = insert(table).values(entry_dict)
#                     session.execute(stmt)
#                 except Exception as e:
#                     print(f"Error adding record to table {table_name}: {e}")
                    
#             try:
#                 session.commit()
#             except Exception as e:
#                 print(f"Error committing session for table {table_name}: {e}")
#                 session.rollback()
#     finally:
#         session.close()




# if __name__ == '__main__':
#     # Parse the log file
#     file_path = '../rsync/qor/fermi.txt'
#     data = parse_fermi_file(file_path)

#     # Set up the database engine
#     engine = create_engine(DATABASE_URL)

#     # Create tables
#     create_tables_from_log(data)

#     # # Insert data
#     insert_data_to_tables(data)








































# import os

# def merge_sect(parsed_groups):
#     # Define group mappings
#     groups = {
#         'group1': {'gpu', 'machine_name', 'design_size'},
#         'group2': {'high_curvature_internal_checking_count', 'mrc_area_count'},
#         'group3': {'mean_fermi'},
#         'group4': {'target_prep_runtime'}
#     }
    
#     # Initialize result dictionary
#     result_dict = {group: [] for group in groups}
    
#     # Process parsed_groups
#     for item in parsed_groups:
#         lines = item.split('\n')
#         if not lines:
#             continue

#         first_line = lines[0]
#         key = first_line.split(' = ', 1)[0]
#         remaining_lines = '\n'.join(lines[1:])
        
#         # Append to the appropriate group
#         for group, keys in groups.items():
#             if key in keys:
#                 result_dict[group].append(first_line + '\n' + remaining_lines)
#                 break
    
#     # Collect results and apply swaps
#     output_list = [ '\n'.join(result_dict.get(group, [])) for group in ['group1', 'group2', 'group3', 'group4'] ]
    
#     # Swap the specified elements
#     output_list[1], output_list[3] = output_list[3], output_list[1]
#     output_list[2], output_list[3] = output_list[3], output_list[2]

#     return output_list

# def parse_logfile(logfile_path, output_file_path):
#     parsed_groups = []
#     current_group = []
    
#     try:
#         with open(logfile_path, 'r') as logfile:
#             for line in logfile:
#                 stripped_line = line.strip()
#                 if stripped_line == "":
#                     if current_group:
#                         parsed_groups.append("\n".join(current_group))
#                         current_group = []
#                 elif '=' in stripped_line:
#                     key, value = stripped_line.split('=', 1)
#                     key, value = key.strip(), value.strip()
#                     current_group.append(f"{key} = {value}")
            
#             if current_group:
#                 parsed_groups.append("\n".join(current_group))
#     except IOError as e:
#         print(f"Error reading file {logfile_path}: {e}")
#         return []
    
#     output_list = merge_sect(parsed_groups)

#     headers = [
#         '[Main_Stats]',
#         '[Runtime_Analysis_Stats]',
#         '[Geometric_Analysis_Stats_Fermi]',
#         '[Statistical_Analysis]'
#     ]
    
#     # Ensure the number of headers matches the number of groups
#     if len(headers) != len(output_list):
#         raise ValueError("The number of headers does not match the number of output list elements.")
    
#     try:
#         with open(output_file_path, 'w') as output_file:
#             for header, group in zip(headers, output_list):
#                 output_file.write(header + "\n")
#                 output_file.write(group + "\n\n")  
#     except IOError as e:
#         print(f"Error writing file {output_file_path}: {e}")
    
#     print(f"Data extracted from input file {logfile_path} and written to {output_file_path}")
#     return output_list

# def main():
#     logfile_path = "../logs/dummy_logfile.txt"
#     output_file_path = "../fermi.txt"
    
#     if os.path.exists(logfile_path):
#         print(f"The input file namely {logfile_path} exists")
#     else:
#         print("File does not exist")
#         return
    
#     output_list = parse_logfile(logfile_path, output_file_path)
#     if output_list:
#         print("Parsing complete")

# if __name__ == "__main__":
#     main()






























# def merge_sect(parsed_groups):
#     result_dict = {
#         'group1': [],
#         'group2': [],
#         'group3': [],
#         'group4': []
#     }
    
#     group1 = ['gpu', 'machine_name', 'design_size']
#     group2 = ['high_curvature_internal_checking_count', 'mrc_area_count']
#     group3 = ['mean_fermi']
#     group4 = ['target_prep_runtime']

#     for item in parsed_groups:
#         lines = item.split('\n')
#         first_line = lines[0]
#         key = first_line.split(' = ', 1)[0]
#         remaining_lines = '\n'.join(lines[1:])
        
#         if key in group1:
#             result_dict['group1'].append(first_line + '\n' + remaining_lines)
#         elif key in group2:
#             result_dict['group2'].append(first_line + '\n' + remaining_lines)
#         elif key in group3:
#             result_dict['group3'].append(first_line + '\n' + remaining_lines)
#         elif key in group4:
#             result_dict['group4'].append(first_line + '\n' + remaining_lines)
    
#     output_list = []
#     for group in ['group1', 'group2', 'group3', 'group4']:
#         if result_dict[group]:
#             output_list.append('\n'.join(result_dict[group]))

#     output_list[1], output_list[3] = output_list[3], output_list[1]
#     output_list[2], output_list[3] = output_list[3], output_list[2]

#     return output_list























# def merge_sect(parsed_groups):
#     result_dict = {}

#     for item in parsed_groups:
#         lines = item.split('\n')
#         first_line = lines[0]
#         key = first_line.split(' = ', 1)[0]
#         remaining_lines = '\n'.join(lines[1:])
        
#         if key in result_dict:
#             # If the key exists, append the remaining lines
#             result_dict[key] += '\n' + first_line + '\n' + remaining_lines
#         else:
#             # If the key doesn't exist, create a new entry using the key
#             result_dict[key] = first_line + '\n' + remaining_lines
    
#     output_list = []
#     for _, value in result_dict.items():
#         output_list.append(f"{value}")

    # return output_list






















# import os
# def parse_logfile(logfile_path, output_file):
#     additional_lines = [
#         "[Main_Stats]",
#         "[Runtime_Analysis_Stats]",
#         "[Geometric_Analysis_Stats_Fermi]",
#         "[Statistical_Analysis]"
#     ]
#     with open(logfile_path, 'r') as logfile, open(output_file, "w") as file:
#         index = 0
#         for line in logfile:
#             stripped_line = line.strip()
#             if stripped_line == "":
#                 file.write("\n")
#                 if index < len(additional_lines):
#                     file.write(f"{additional_lines[index]}\n")
#                     index += 1
#             elif '=' in stripped_line:
#                 key, value = stripped_line.split('=', 1)
#                 key, value = key.strip(), value.strip()
#                 file.write(f"{key} = {value}\n")

#         print(f"Data extracted from input file {logfile_path}")
#         print(f"Data written to the output file {output_file}")
    
# def main():
#     logfile_path = "dummy_logfile.txt"
#     if os.path.exists(logfile_path):
#         print(f"The input file namely {logfile_path} exists")
#     else:
#         print("File does not exist")
#     output_file = "generated.txt"
#     parse_logfile(logfile_path, output_file)
#     print("Parsing complete")

# if __name__ == "__main__":
#     main()




# import os
# def parse_logfile(logfile_path, output_file):
    
#     with open(logfile_path, 'r') as logfile, open(output_file, "w") as file:
#         for line in logfile:
#             stripped_line = line.strip()
#             if stripped_line == "":
#                 file.write("\n")
                
#             elif '=' in stripped_line:
#                 key, value = stripped_line.split('=', 1)
#                 key, value = key.strip(), value.strip()
#                 file.write(f"{key} = {value}\n")

#         print(f"Data extracted from input file {logfile_path}")
#         print(f"Data written to the output file {output_file}")
    
# def main():
#     logfile_path = "dummy_logfile.txt"
#     if os.path.exists(logfile_path):
#         print(f"The input file namely {logfile_path} exists")
#     else:
#         print("File does not exist")
#     output_file = "generated.txt"
#     parse_logfile(logfile_path, output_file)
#     print("Parsing complete")

# if __name__ == "__main__":
#     main()





# import os
# def parse_logfile(logfile_path, output_file):
#     additional_lines = [
#         "[Main_Stats]",
#         "[Runtime_Analysis_Stats]",
#         "[Geometric_Analysis_Stats_Fermi]",
#         "[Statistical_Analysis]"
#     ]
#     with open(logfile_path, 'r') as logfile, open(output_file, "w") as file:
#         index = 0
#         for line in logfile:
#             stripped_line = line.strip()
#             if stripped_line == "":
#                 file.write("\n")
#                 if index < len(additional_lines):
#                     file.write(f"{additional_lines[index]}\n")
#                     index += 1
#             elif '=' in stripped_line:
#                 key, value = stripped_line.split('=', 1)
#                 key, value = key.strip(), value.strip()
#                 file.write(f"{key} = {value}\n")

#         print(f"Data extracted from input file {logfile_path}")
#         print(f"Data written to the output file {output_file}")
    
# def main():
#     logfile_path = "dummy_logfile.txt"
#     if os.path.exists(logfile_path):
#         print(f"The input file namely {logfile_path} exists")
#     else:
#         print("File does not exist")
#     output_file = "generated.txt"
#     parse_logfile(logfile_path, output_file)
#     print("Parsing complete")

# if __name__ == "__main__":
#     main()












































# import os

# def parse_logfile(logfile_path, output_file):
#     fermi_data = {}
#     with open(logfile_path, 'r') as logfile:
#         for line in logfile:
#             if '=' in line:
#                 key, value = line.strip().split('=')
#                 fermi_data[key.strip()] = value.strip()
#         print(f"Data extracted from input file {logfile_path}")

#     with open(output_file, "w") as file:
#         for key, value in fermi_data.items():
#             file.write(f"{key} = {value}\n")
#         print(f"Data written to the output file {output_file}")
    
# def main():
#     logfile_path = "dummy_logfile.txt"
#     if os.path.exists(logfile_path):
#         print(f"The input file namely {logfile_path} exists")
#     else:
#         print("File does not exist")
#     output_file = "generated.txt"
#     parse_logfile(logfile_path, output_file)
#     print("Parsing complete")

# if __name__ == "__main__":
#     main()




