from datetime import datetime
import pymysql
from ..Functions.config import Config
from ..Controllers.LogsHandler import Logs

class Connect (object):
    def __init__(self):
        self.user = Config['dbuser']
        self.password = Config['dbpass']
        self.host = Config['dbhost']
        self.database = Config['dbname']
        self.port = Config['dbport']
        self.conn = ""
        self._query_execute = ""
        
    def connect(self):
        try:
            self.conn = pymysql.connect(user=self.user, password=self.password , host=self.host, db=self.database, port=self.port)
            self._query_execute = self.conn.cursor()
            if self._query_execute:
                Logs.recordLogs("Success: Connection to database succeeded")
                return self._query_execute
        except Exception as e:
            Logs.recordLogs(f"DatabaseConnectionException: {str(e)}")
        