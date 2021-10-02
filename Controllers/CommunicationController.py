import telnyx
from .LogsHandler import Logs
from ..DBF.DBConnect import Connect
from ..DBF.DBFunctions import DBFunctions
from ..Functions.config import Config

class Communication(object):
    def __init__(self):
        pass
    

    @staticmethod
    def sendEmail(to_email, subject, body):
        try:
            pass
        except Exception as exc:
            Logs.recordLogs(f"EmailException: {str(exc)}")
    
    @staticmethod
    def sendSms(to_number, body):
        try:
            telnyx.api_key = Config['telnyx_api_key']
            response = telnyx.Message.create(
                from_= Config['telnyx_number'],
                to = to_number,
                text = body,
            )
            Logs.recordLogs(f"sendEmail, response: {str(response)}")
        except Exception as exc:
            Logs.recordLogs(f"SmsException: {str(exc)}")