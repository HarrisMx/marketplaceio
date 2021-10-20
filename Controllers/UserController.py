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

            ''' fullname = request.json['fullname']
            email = request.json['email']
            password = request.json['password'] '''

            Logs.recordLogs(f"registerUser data: {phone_number} ,{id_number}")
            res = dbfObj.RegisterUser(phone_number, id_number)
            try:
                jwt_token = jwt.encode({
                    'user_token': res[0],
                    'sessions_expires_on': str(datetime.utcnow() + timedelta(minutes = 5))
                },
                Config['secret_key'],
                algorithm="HS256")
                return jsonify({"Success": True, "messages": ["Validation Sucess", "You will recieve an OTP to confirm your number shortly."], "token": jwt_token})
            except Exception as exc:
                Logs.recordLogs(f"JWTEncodeError: {str(exc)}")
            
        except Exception as exc:
            Logs.recordLogs(f"RegistrationException: {str(exc)}")
    
    @staticmethod
    def getOTP(request):
        try:
            dbfObj = DBFunctions()
            otp_number = request.json['otp_number']
            token = request.json['uToken']

            Logs.recordLogs(f"registerUser data: {otp_number} ,{token}")

            try:
                #decoded = jwt.decode(token, options={"verify_signature": False})
                decoded = jwt.decode(token, Config['secret_key'], algorithms=["RS256"])
                Logs.recordLogs(f"registerUser decoded: {decoded}")
                sessions_expires_on = datetime.strptime(decoded['sessions_expires_on'], '%m-%d-%Y %H:%M')

                if sessions_expires_on <= datetime.utcnow():
                    return jsonify({"Success": True, "messages": [], "token": token})
                else:
                    return jsonify({"Success": False, "messages": ["OTP code expired"], "token": token})
            except Exception as exc:
                Logs.recordLogs(f"JWTEncodeError: {str(exc)}")
            
        except Exception as exc:
            Logs.recordLogs(f"OTPException: {str(exc)}")
            return jsonify({"Success": False, "messages": ["OTP Verification failed"], "token": token})