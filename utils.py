import random
import Point as Pt
import Ship


class BoardUtils:
    ships = []
    board = []

    def __init__(self, size_h, size_v):
        self.size_h = size_h
        self.size_v = size_v
        self.board = [['-' for x in range(size_h)] for y in range(size_v)]
        self.place_ships()
        self.score = 0
        self.shots = 0

    def draw_board(self):
        for y in range(self.size_v):
            for x in range(self.size_h):
                print(self.board[y][x] + ' ', end='')
            print()

    def compare_point(self, point_a, point_b):
        return (point_a.get_x() == point_b.get_x()) and (point_a.get_y() == point_b.get_y())

    def stike(self, point):
        self.shots += 1
        for ship in self.ships:
            for ship_part in ship.get_parts():
                if self.compare_point(point, ship_part):
                    print('Trafiony')
                    ship.ship_parts.pop(0)
                    self.board[ship_part.get_y()][ship_part.get_x()] = 'x'
                    print('Score: {}'.format(ship.get_length()))
                    if ship.get_length() == 0:
                        self.score += 1
                        self.ships.pop()
                    return
        self.board[point.get_y()][point.get_x()] = 'o'

    def place_ships(self):
        for ship in self.ships:
            for ship_part in ship.get_parts():
                self.board[ship_part.get_y()][ship_part.get_x()] = '\u2588'

    def get_ships_count(self):
        return len(self.ships)

    def rand_ships(self, count, length, orientation):
        while count != 0:
            x = random.randint(1, self.size_h - (length + 1))
            y = random.randint(1, self.size_v - (length + 1))
            point = Pt.Point(x, y)
            if not self.is_collision(point, length, orientation):
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

    def get_score(self):
        return self.score

    def get_shots_count(self):
        return self.shots