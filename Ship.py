import Point

class Ship:
    def __init__(self, coordinate, length):
        self.coordinate = coordinate
        self.length = length
    def getCoordinates(self):
        return [self.coordinate.getX(), self.coordinate.getY()]
    def getLength(self):
        return self.length
