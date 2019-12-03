class Ship:
    def __init__(self, x, y, type, axis):
        self.x = x
        self.y = y
        self.type = type
        self.axis = axis
    def getCoordinates(self):
        return [self.x, self.y]
    def getType(self):
        return self.type
    def getAxis(self):
        return self.axis