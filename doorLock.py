

class doorLock(roomModule):
   
    statusCode#0 == unlocked 1== locked
    statusColorUnlocked = '#66DC00'
    statusColorLocked = '#FC1500'

    def __init__(self):
        super(self, 'Door Lock')
    
    def getStatus(self):
        color = ((self.statusCode == 1) ? statusColorLocked : statusColorUnlocked)
        return super.generateStatus(self.statusCode, 'door is in some state', color)
  
    def receivePacket(self):  
