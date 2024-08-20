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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/geometric-analysis', methods=['GET'])
def get_geometric_analysis():
    query = text('SELECT * FROM Geometric_Analysis_Stats_Fermi')
    with engine.connect() as connection:
        result = connection.execute(query)
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result.fetchall()]
    return render_template('geometric_analysis.html', data=data)

@app.route('/main-stats', methods=['GET'])
def get_main_stats():
    query = text('SELECT * FROM Main_Stats')
    with engine.connect() as connection:
        result = connection.execute(query)
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result.fetchall()]
    return render_template('main_stats.html', data=data)

@app.route('/runtime-analysis', methods=['GET'])
def get_runtime_analysis():
    query = text('SELECT * FROM Runtime_Analysis_Stats')
    with engine.connect() as connection:
        result = connection.execute(query)
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result.fetchall()]
    return render_template('runtime_analysis.html', data=data)

@app.route('/statistical-analysis', methods=['GET'])
def get_statistical_analysis():
    query = text('SELECT * FROM Statistical_Analysis')
    with engine.connect() as connection:
        result = connection.execute(query)
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result.fetchall()]
    return render_template('statistical_analysis.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=7000)
