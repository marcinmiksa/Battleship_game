from Field import Field
from Stats import Stats
from FieldType import FieldType


class ShipPart(Field):
    def __init__(self, point, status):
        super().__init__(point, status)
        Stats.ship_counter += 1

    def get_type(self):
        return FieldType.SHIP
