import random
from Field import Field
from ShipPart import ShipPart
from Point import Point
from Shot import Shot


class Board:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.fields = []
        self.create()

    def create(self):
        for y in range(self.size_y):
            self.fields.append([])
            for x in range(self.size_x):
                self.fields[y].append(Field(Point(x, y), True))

    def draw(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.fields[y][x].get_status():
                    print('  ', end='')
                else:
                    if isinstance(self.fields[y][x], ShipPart):
                        print('\u2588 ', end='')
                    else:
                        print('x ', end='')
            print()

    def is_free_place(self, point, length):
        for i in range(length):
            if isinstance(self.fields[point.get_y()][point.get_x() + i], ShipPart):
                return False
        return True

    def rand_ship(self, length):
        while True:
            x = random.randint(1, self.size_x - (length + 1))
            y = random.randint(1, self.size_y - (length + 1))
            if self.is_free_place(Point(x, y), length):
                for i in range(length):
                    self.fields[y][x + i] = ShipPart(Point(x + i, y), True)
                break

    def strike(self, point):
        if self.fields[point.get_y()][point.get_x()].get_status():
            self.fields[point.get_y()][point.get_x()].set_status(False)
            if isinstance(self.fields[point.get_y()][point.get_x()], ShipPart):
                ShipPart.counter -= 1
                return Shot.SHOT_SUCCESSFUL
            else:
                return Shot.SHOT_UNSUCCESSFUL
        return Shot.SHOT_REPEATED

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y
