from flask import Flask
from flask_cors import CORS

from Modules.connect import connect_to_db
from Modules.data import get_data

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/gettestresult')
def get_test_result():
    connection = connect_to_db()
    get_data(connection)
    return "Mail pop up"

