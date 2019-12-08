import random
import Point as pt
import Ship as ship

class ShipUtils:
    ships = []
    def addShip(self, point, length, type):
        self.ships.append(ship.Ship(point, length, type))

    def randShips(self, amount):
        for i in range(ammount):
            self.addShip(pt.Point())

    def getShips(self):
        return self.ships

class BoardUtils:
    size = 0
    shipUtils = ShipUtils()
    def initBoard(self, size):
        self.size = size
        self.board = [['#' for x in range(size)] for y in range(size)]
        self.shipUtils.addShip(pt.Point(1, 1), 4, 'h')
        self.shipUtils.addShip(pt.Point(4, 4), 3, 'v')
        self.placeShips()

    def drawBoard(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.board[y][x] + ' ', end='')
            print()

    def placeShips(self):
        for ship in self.shipUtils.getShips():
            coordinateX = ship.getCoordinateX()
            coordinateY = ship.getCoordinateY()
            for part in range(ship.getLength()):
                if ship.getType() == 'h':
                    coordinateY += 1
                else:
                    coordinateX += 1
                self.board[coordinateY][coordinateX] = 'o'

