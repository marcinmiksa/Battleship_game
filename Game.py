from Board import Board
from Point import Point
from Stats import Stats
from GameView import GameView


class Game:
    def __init__(self):
        self.stats = Stats()
        self.game_view = GameView()

    def create_view(self):
        self.game_view.read_dimentions()

    def put_ships(self):
        print('\n*** Dodawanie statkow ***')
        for ship_type in range(1, 5):
            ships_count = int(input('Ile statkow {}-elementowych dodac: '.format(ship_type)))
            for i in range(ships_count):
                self.game_view.board.rand_ship(ship_type)

    def run(self):
        while Stats.ship_counter > 0:
            x = int(input('Podaj wspolrzedna x strzalu: '))
            y = int(input('Podaj wspolrzedna y strzalu: '))
            if x > (self.game_view.board.get_size_x() - 1) or x < 0 or y > (
                    self.game_view.board.get_size_y() - 1) or y < 0:
                print('\nWybrano punkt poza zakresem. Sprobuj ponownie\n')
                continue
            strike = self.game_view.board.strike(Point(x, y))
            if strike == 1:
                self.stats.increase_successful_shots_count()
            elif strike == -1:
                print('\nStrzal zostal powtorzony. Wybierz inne pole\n')
                continue
            else:
                self.stats.increase_missed_shots_count()
            self.game_view.draw_board()
        self.stats.display_stats()
