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
    board = []

    def __init__(self, size):
        self.size = size
        self.board = [['-' for x in range(size)] for y in range(size)]
        self.ships.append(Ship.Ship(Pt.Point(0, 0), 5, 'h', True))
        # self.ships.append(Ship.Ship(Pt.Point(6, 5), 4, 'v', True))
        # self.ship_utils.add_ship(Pt.Point(4, 4), 3, 'v', True)
        # self.ship_utils.add_ship(Pt.Point(8, 8), 1, 'v', True)
        # self.ship_utils.add_ship(Pt.Point(6, 7), 2, 'v', True)
        self.place_ships()
        print(self.is_collision(Pt.Point(2, 0), 3, 'h'))
        print(self.is_collision(Pt.Point(5, 5), 4, 'v'))

    def draw_board(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.board[y][x] + ' ', end='')
            print()

    def place_ships(self):
        for ship in self.ships:
            for ship_part in ship.get_parts():
                self.board[ship_part.get_y()][ship_part.get_x()] = '\u2588'

    def is_collision(self, point, ship_length, orientation):
        if orientation == 'h':
            if self.board[point.get_y()][point.get_x() - 1] != '-' or \
                    self.board[point.get_y()][point.get_x() + ship_length] != '-':
                return True
            for i in range(ship_length):
                if self.board[point.get_y() + 1][point.get_x() + i] != '-' or \
                        self.board[point.get_y() - 1][point.get_x() + i] != '-':
                    return True
        else:
            if self.board[point.get_y() - 1][point.get_x()] != '-' or \
                    self.board[point.get_y() + ship_length][point.get_x()] != '-':
                return True
            for i in range(ship_length):
                if self.board[point.get_y() + i][point.get_x() + 1] != '-' or \
                        self.board[point.get_y() + i][point.get_x() - 1] != '-':
                    return True
        return False
