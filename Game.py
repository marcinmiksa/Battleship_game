from Board import Board
from Point import Point
from Stats import Stats
from ShipPart import ShipPart


class Game:
    def __init__(self):
        self.board = None
        self.read_board_size()
        self.put_ships()
        self.stats = Stats()

    def read_board_size(self):
        board_size_x = int(input('Podaj wymiar planszy w poziomie: '))
        board_size_y = int(input('Podaj wymiar planszy w pionie: '))
        self.board = Board(board_size_x, board_size_y)

    def put_ships(self):
        print('\n*** Dodawanie statkow ***')
        for ship_type in range(1, 5):
            ships_count = int(input('Ile statkow {}-elementowych dodac: '.format(ship_type)))
            for i in range(ships_count):
                self.board.rand_ship(ship_type)

    def run(self):
        while ShipPart.counter > 0:
            x = int(input('Podaj wspolrzedna x strzalu: '))
            y = int(input('Podaj wspolrzedna y strzalu: '))
            if x > (self.board.get_size_x() - 1) or x < 0 or y > (self.board.get_size_y() - 1) or y < 0:
                print('\nWybrano punkt poza zakresem. Sprobuj ponownie\n')
                continue
            strike = self.board.strike(Point(x, y))
            if strike == 1:
                self.stats.increase_successful_shots_count()
            elif strike == -1:
                print('\nStrzal zostal powtorzony. Wybierz inne pole\n')
                continue
            else:
                self.stats.increase_missed_shots_count()
            self.board.draw()
        self.stats.display_stats()
