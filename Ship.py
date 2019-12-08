import Point

class Ship:
    def __init__(self, coordinate, length, type):
        self.coordinate = coordinate
        self.length = length
        self.type = type
    def getCoordinateX(self):
        return self.coordinate.getX()
    def getCoordinateY(self):
        return self.coordinate.getY()
    def getLength(self):
        return self.length
    def getType(self):
        return self.type
