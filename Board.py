import random
from Field import Field
from ShipPart import ShipPart
from Point import Point
from Shot import Shot
from Stats import Stats
from FieldType import FieldType


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

    def get_field(self, point):
        return self.fields[point.get_y()][point.get_x()]

    def is_free_place(self, point, length, orientation):
        for i in range(length):
            if self.fields[point.get_y()][point.get_x() + i].get_type() == FieldType.SHIP:
                return False
            if orientation:
                point.set_x(point.get_x() + i)
            else:
                point.set_y(point.get_y() + i)
        return True

    def place_ship(self, point, length, orientation):
        for i in range(length):
            self.fields[point.y][point.x] = ShipPart(point, True)
            if orientation:
                point.x += 1
            else:
                point.y += 1

    def rand_ship(self, length):
        while True:
            x = random.randint(0, self.size_x - (length + 1))
            y = random.randint(0, self.size_y - (length + 1))
            orientation = random.randint(0, 1)
            if self.is_free_place(Point(x, y), length, orientation):
                self.place_ship(Point(x, y), length, orientation)
                break

    def strike(self, point):
        if self.fields[point.get_y()][point.get_x()].get_status():
            self.fields[point.get_y()][point.get_x()].set_status(False)
            if self.fields[point.get_y()][point.get_x()].get_type() == FieldType.SHIP:
                Stats.ship_counter -= 1
                return Shot.SHOT_SUCCESSFUL
            else:
                return Shot.SHOT_UNSUCCESSFUL
        return Shot.SHOT_REPEATED

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y
