from datetime import datetime
from flask import jsonify
import os
import time
from .LogsHandler import Logs
from ..DBF.DBConnect import Connect
from ..DBF.DBFunctions import DBFunctions

class UserHandler (object):
    def __init__(self):
        pass

    @staticmethod
    def loginUser(request):
        try:
            dbfObj = DBFunctions()
            username = request.json['email']
            password = request.json['password']
            Logs.recordLogs(f"LoginDetails: username {username}, password {password}")
            res = dbfObj.LoginUser(username, password)
            Logs.recordLogs(f"LoginToken: {str(res[0])}")
            return jsonify({"Success": True, "message": "Login Success", "Token": res[0]})
        except Exception as exc:
            Logs.recordLogs(f"LoginException: {str(exc)}")
    
    @staticmethod
    def registerUser(request):
        try:
            dbfObj = DBFunctions()
            phone_number = request.json['contact_number']
            id_number = request.json['id_number']
            Logs.recordLogs(f"registerUser: phone_number {phone_number}, id_number {id_number}")
            dbfObj.RegisterUser(phone_number, id_number)
            return jsonify({"Success": True, "messages": ["Registration Success", "You will recieve an sms confirming your registration shortly."], "Token": res[0]})
        except Exception as exc:
            Logs.recordLogs(f"RegistrationException: {str(exc)}")