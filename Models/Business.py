from person import Person

class Business(Person):
    def __init__(self, name, surname, username, password, address, coordinates):
        super(Person, self).__init__()
        self.address = address
        self.coordinates = coordinates
        
    def getAddress(self):
        return self.address
    
    def getCoordinates(self):
        return self.coordinates