class Person(object):
    def __init__(self):
        super().__init__()
        self.name = ''
        self.surname = ''
        self.username = ''
        self.password = ''
        
    def setPerson(self, name, surname, username, password):
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
    
    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname
    
    def getUsername(self):
        return self.username
    
    def validateInfomation(self):
        try:
            if len(self.name) == 0:
                return False;
            elif len(self.surname) == 0:
                return False
            
        except Exception as exc:
            return "Exception caught: {} ".format(exc);