import Point


class Ship:

    def __init__(self, coordinate, length, ship_type, status):
        self.coordinate = coordinate
        self.length = length
        self.ship_type = ship_type
        self.status = status
        self.ship_parts = []
        self.set_parts(coordinate, length, ship_type)

    def set_parts(self, head_coordinate, length, ship_type):
        for i in range(length):
            if ship_type == 'h':
                self.ship_parts.append(Point.Point((head_coordinate.get_x() + i), head_coordinate.get_y()))
            else:
                self.ship_parts.append(Point.Point(head_coordinate.get_x(), (head_coordinate.get_y() + i)))

    def get_coordinate_x(self):
        return self.coordinate.get_x()

    def get_coordinate_y(self):
        return self.coordinate.get_y()

    def get_length(self):
        return len(self.ship_parts)

    def get_ship_type(self):
        return self.ship_type

    def get_status(self):
        return self.status

    def get_parts(self):
        return self.ship_parts
