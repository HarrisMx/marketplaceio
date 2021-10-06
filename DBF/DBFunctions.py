from .DBConnect import Connect

class DBFunctions(object):
    def __init__(self):
        self.dbconn = Connect()
        self.qryConn = self.dbconn.connect()
    
    def LoginUser(self, username, password):
        self.qryConn.callproc("spLoginUser", [username, password])
        res = self.qryConn.fetchone()
        return res
    
    def RegisterUser(self, phone_number, id_number, fullname, email, password):
        self.qryConn.callproc("spRegisterUser", [phone_number, id_number, fullname, email, password])
        res = self.qryConn.fetchone()
        return res
