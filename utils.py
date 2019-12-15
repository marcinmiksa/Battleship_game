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
    ship_utils = ShipUtils()
    ships = []
    board = []

    def __init__(self, size_h, size_v):
        self.size_h = size_h
        self.size_v = size_v
        self.board = [['-' for x in range(size_h)] for y in range(size_v)]
        self.rand_ships(1, 1, 'v')
        self.rand_ships(3, 2, 'h')
        self.rand_ships(1, 3, 'v')
        self.place_ships()

    def draw_board(self):
        for y in range(self.size_v):
            for x in range(self.size_h):
                print(self.board[y][x] + ' ', end='')
            print()

    def place_ships(self):
        for ship in self.ships:
            for ship_part in ship.get_parts():
                self.board[ship_part.get_y()][ship_part.get_x()] = '\u2588'

    def rand_ships(self, count, length, orientation):
        while count != 0:
            x = random.randint(1, self.size_h - (length + 1))
            y = random.randint(1, self.size_v - (length + 1))
            point = Pt.Point(x, y)
            if not self.is_collision(point, length, orientation):
                print('{}, {}\n'.format(x, y))
                self.ships.append(Ship.Ship(point, length, orientation, True))
                self.place_ships()
                count -= 1

    def is_collision(self, point, ship_length, orientation):
        if orientation == 'h':
            for i in range(ship_length):
                if self.board[point.get_y() - 1][point.get_x() + i] != '-' or \
                        self.board[point.get_y() + 1][point.get_x() + i] != '-':
                    return True
            for i in range(-1, 1):
                if self.board[point.get_y() + i][point.get_x() - 1] != '-' or \
                        self.board[point.get_y() + i][point.get_x() + ship_length] != '-':
                    return True
        else:
            for i in range(ship_length):
                if self.board[point.get_y() + i][point.get_x() - 1] != '-' or \
                        self.board[point.get_y() + i][point.get_x() + 1] != '-':
                    return True
            for i in range(-1, 1):
                if self.board[point.get_y() - 1][point.get_x() + i] != '-' or \
                        self.board[point.get_y() + ship_length][point.get_x() + i] != '-':
                    return True
        return False
