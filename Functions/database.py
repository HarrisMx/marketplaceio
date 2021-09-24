import pymysql

class Database(object):
    
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.conn = ""
        self._query_execute = ""
        
    def connect(self):
        try:
            self.conn = pymysql.connect(user=self.user, password=self.password , host=self.host, db=self.database)
            #self.conn.autocommit(True)
            self._query_execute = self.conn.cursor()
            if self._query_execute:
                print("Success: Connection to database succeeded")
        except Exception as e:
            print("Error: ", e)
        return self._query_execute