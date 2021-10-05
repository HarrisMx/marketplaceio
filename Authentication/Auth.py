from flask import session, jsonify
from datetime import datetime, timedelta
from functools import wraps
import jwt
from ..DBF.DBFunctions import DBFunctions
from ..Functions.Functions import LogsHandler
from ..Functions.config import Config

class Authentication(object):
    def __init__(self):
        pass

    @staticmethod
    def authenticateLogin(request):
        try:
            bdf = DBFunctions()
            username = request.json['email']
            password = request.json['password']
            res = bdf.LoginUser(username, password)

            if res is not None and len(res[0]) > 5:
                session['valid_user_token'] = res[0]
                jwt_token = jwt.encode({
                    'user_token': res[0],
                    'sessions_expires_on': str(datetime.utcnow() + timedelta(hours = 8))
                },
                Config['secret_key']
                )
                return jsonify({'auth_token': jwt_token, 'Success': True, "Message": "Login Success"})
            else:
                return jsonify({'Success': False, "Message": "Login Failed"})
        except Exception as exc:
            LogsHandler.recordLogs(f"LoginException : {str(exc)}")

    @staticmethod
    def logoutUser(request):
        try:
            pass
        except Exception as exc:
            LogsHandler.recordLogs(f"LogoutException : {str(exc)}")
