
class roomModule:
    
    name

    def __init__(self, name):
        self.name = name

    def generateStatus(self, code, message, color):
        return {'statusCode' : code, 'status' : message, 'statucColorCode' : color} 

    def receivePacket(self);
        pass

    def getStatus(self):
        return self.generateStatus(-1, 'No getStatus defined', '#000000')
     
   
