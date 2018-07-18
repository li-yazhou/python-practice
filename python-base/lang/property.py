class Property(object):
    def __init__(self,size=10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)
