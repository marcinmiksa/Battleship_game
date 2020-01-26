from FieldType import FieldType
from Board import Board
from Point import Point


class GameView:
    def __init__(self):
        self.board = None

    def read_dimentions(self):
        board_size_x = int(input('Podaj wymiar planszy w poziomie: '))
        board_size_y = int(input('Podaj wymiar planszy w pionie: '))
        self.create_board(board_size_x, board_size_y)

    def create_board(self, board_size_x, board_size_y):
        self.board = Board(board_size_x, board_size_y)
        self.board.create()

    def draw_board(self):
        for y in range(self.board.size_y):
            for x in range(self.board.size_x):
                if self.board.get_field(Point(x, y)).get_status():
                    print('  ', end='')
                else:
                    if self.board.get_field(Point(x, y)).get_type() == FieldType.SHIP:
                        print('\u2588 ', end='')
                    else:
                        print('x ', end='')
            print()

    def add_field(self):
        self.fields.append()