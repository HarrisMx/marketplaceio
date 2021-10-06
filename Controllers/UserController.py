from datetime import datetime, timedelta
from flask import jsonify
import os
import time
import jwt
from .LogsHandler import Logs
from ..DBF.DBConnect import Connect
from ..DBF.DBFunctions import DBFunctions
from ..Functions.config import Config

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
    def registerUser(request): #CALL spRegisterUser(0817302568, 561212472084, "John Doe", "john@email.com", "John@doe123"); 
        try:
            dbfObj = DBFunctions()
            phone_number = request.json['contact_number']
            id_number = request.json['id_number']
            fullname = request.json['fullname']
            email = request.json['email']
            password = request.json['password']

            Logs.recordLogs(f"registerUser data: {phone_number} ,{id_number} ,{fullname} ,{email} ,{password}")
            res = dbfObj.RegisterUser(phone_number, id_number, fullname, email, password)
            try:
                jwt_token = jwt.encode({
                    'user_token': res[0],
                    'sessions_expires_on': str(datetime.utcnow() + timedelta(hours = 8))
                },
                Config['secret_key'],
                algorithm="HS256")
                return jsonify({"Success": True, "messages": ["Registration Success", "You will recieve an sms confirming your registration shortly."], "auth_token": jwt_token})
            except Exception as exc:
                Logs.recordLogs(f"JWTEncodeError: {str(exc)}")
            
        except Exception as exc:
            Logs.recordLogs(f"RegistrationException: {str(exc)}")