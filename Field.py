class Field:
    def __init__(self, point, status):
        self.point = point
        self.status = status

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
