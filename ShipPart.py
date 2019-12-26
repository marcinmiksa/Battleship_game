from Field import Field


class ShipPart(Field):
    counter = 0

    def __init__(self, point, status):
        super().__init__(point, status)
        ShipPart.counter += 1
