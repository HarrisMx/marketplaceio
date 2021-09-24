from flask import Flask, request, jsonify, make_response, url_for, abort
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
from .Controllers.BusinessController import BusinessHandler
from .Controllers.UserController import UserHandler
from .Controllers.LogsHandler import Logs
import time
import json
from datetime import datetime
from datetime import date
import os

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = "*"
app.config['DEBUG'] = True

cors = CORS(app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'kasi101':
        return 'R3qu3st3r2014'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.route('/', methods=['GET'])
def home():
    return json.dumps({"Success": True, "Message": "Welcome to MarketplaceIo API."}, indent=4)


'''
    User Handler Endpoints
'''

@app.route('/api/User/Login', methods=['POST'])
def Login():
    try:
        response = UserHandler.loginUser(request)
        return response
    except Exception as exc:
        recordLogs(f"Entry Exception: {str(exc)}")

@app.route('/api/User/Register', methods=['POST'])
def Register():
    try:
        response = UserHandler.registerUser(request)
        return response
    except Exception as exc:
        recordLogs(f"Entry Exception: {str(exc)}")

@app.route('/api/User/Profile', methods=['POST'])
def Profile():
    try:
        pass
    except Exception as exc:
        recordLogs(f"Entry Exception: {str(exc)}")

@app.route('/api/User/Profile/Edit', methods=['POST'])
def Edit():
    try:
        pass
    except Exception as exc:
        recordLogs(f"Entry Exception: {str(exc)}")

'''
    Jobs Handler Endpoints
'''

'''
    Hire Tools Handler Endpoints
'''

'''
    Test branch
'''

def recordLogs(msg):
    today = date.today()
    _filename = today.strftime("%d-%m-%Y")
    _filename = f"{str(_filename)}.txt"
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    _filename = os.path.join(os.getcwd(), "Logs", _filename)
    file = open(_filename, "a+")
    file.write(f"{current_time} - {msg}")
    file.write("\n")
    file.close()