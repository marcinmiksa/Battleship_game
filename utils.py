import random
import Point as Pt
import Ship


class ShipUtils:
    ships = []

    def add_ship(self, point, length, ship_type, status):
        self.ships.append(Ship.Ship(point, length, ship_type, status))

    def rand_ships(self, amount):
        for i in range(ammount):
            self.addShip(pt.Point())

    def get_ships(self):
        return self.ships


class BoardUtils:
    size = 0
    ship_utils = ShipUtils()
    ships = []

    def init_board(self, size):
        self.size = size
        self.board = [[' ' for x in range(size)] for y in range(size)]
        self.ships.append(Ship.Ship(Pt.Point(1, 1), 4, 'h', True))
        # self.ship_utils.add_ship(Pt.Point(4, 4), 3, 'v', True)
        # self.ship_utils.add_ship(Pt.Point(8, 8), 1, 'v', True)
        # self.ship_utils.add_ship(Pt.Point(6, 7), 2, 'v', True)
        self.place_ships()

    def draw_board(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.board[y][x] + ' ', end='')
            print()

    def place_ships(self):
        for ship in self.ships:
            for ship_part in ship.get_parts():
                self.board[ship_part.get_y()][ship_part.get_x()] = '\u2588'
