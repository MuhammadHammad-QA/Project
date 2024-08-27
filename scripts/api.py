from flask import Flask, jsonify, request, render_template
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import logging

# Flask app
app = Flask(__name__)

# Database connection details
DATABASE_URL = 'mysql+pymysql://d2s:d2s_1234@localhost/emumba_qor'

# Set up the database engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Configure logging
logging.basicConfig(level=logging.INFO)

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
    
    # Basic validation to avoid SQL injection
    if not table_name.isidentifier():
        return render_template('error.html', message="Invalid table name."), 400

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
    # Retrieve query parameters from the GET request
    job_id = request.args.get('job_id')
    user = request.args.get('user')
    name = request.args.get('name')
    revision = request.args.get('revision')

    # Check if at least one search criterion is provided
    if not job_id and not user and not name and not revision:
        return render_template('error.html', message="Please enter at least one search criterion."), 400

    # Initialize conditions and parameters for the SQL query
    conditions = []
    params = {}

    # Direct match for job_id
    if job_id:
        conditions.append("job_id = :job_id")
        params['job_id'] = job_id
    
    # Add conditions for other fields
    if user:
        conditions.append("(properties = 'user' AND value = :user)")
        params['user'] = user
    if name:
        conditions.append("(properties = 'name' AND value = :name)")
        params['name'] = name
    if revision:
        conditions.append("(properties = 'revision' AND value = :revision)")
        params['revision'] = revision

    # Handle the query for combined criteria
    if job_id:
        if conditions:
            # Create a list to store subqueries for each condition
            subqueries = []
            for condition in conditions:
                subqueries.append(f'''
                    SELECT job_id FROM All_Data
                    WHERE {condition}
                ''')
        
            # Combine all subqueries using INTERSECT to get common job_ids
            subquery = " INTERSECT ".join(f"({subquery})" for subquery in subqueries)
        else:
            subquery = '''
                SELECT DISTINCT job_id FROM All_Data
                WHERE job_id = :job_id
           '''
    else:  
        # Query without job_id
        subquery_conditions = " OR ".join(conditions)
        subquery = f'''
            SELECT DISTINCT job_id FROM All_Data
            WHERE {subquery_conditions}
            GROUP BY job_id
            HAVING COUNT(DISTINCT properties) = {len(conditions)}
        '''
    
    job_id_results = execute_query(subquery, params)

    # If no job_ids are found, return an error
    if not job_id_results:
        return render_template('error.html', message="No matching data found for the given criteria."), 404
    
    job_ids = [row['job_id'] for row in job_id_results]
    
    # If no valid job_ids are found, return an error
    if not job_ids:
        return render_template('error.html', message="No matching data found for the given criteria."), 404
    
    # Fetch all data for the valid job_ids
    job_ids_placeholder = ', '.join([f":job_id{i}" for i in range(len(job_ids))])
    data_query = f'''
        SELECT * FROM All_Data
        WHERE job_id IN ({job_ids_placeholder})
    '''
    
    # Add job_id parameters to the final parameters dictionary
    for i, jid in enumerate(job_ids):
        params[f'job_id{i}'] = jid

    # Execute the query to fetch the data
    data = execute_query(data_query, params)

    # If no data is found, return an error
    if not data:
        return render_template('error.html', message="Data not found for the given criteria."), 404

    # Render the results template with the retrieved data
    return render_template('results.html', data=data, table_name='All_Data')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=7000)

