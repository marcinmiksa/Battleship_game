# TODO: Czyszczenie ekranu
import utils
import Point

def main():
    print('Podaj wymiar planszy w poziomie: ')
    board_dimensions_x = int(input())
    print('Podaj wymiar planszy w pionie: ')
    board_dimensions_y = int(input())
    boardUtils = utils.BoardUtils(board_dimensions_x, board_dimensions_y)

    boardUtils.rand_ships(1, 1, 'v')
    boardUtils.rand_ships(3, 2, 'h')
    boardUtils.rand_ships(1, 3, 'v')

    boardUtils.draw_board()

    while boardUtils.get_ships_count() != 0:
        x = input('Podaj wspolrzedna x strzalu: ')
        y = input('Podaj wspolrzedna y strzalu: ')
        boardUtils.stike(Point.Point(int(x), int(y)))
        boardUtils.draw_board()
        print('Zestrzelonych statkow: {}'.format(boardUtils.get_score()))

    print('*** Statystyki ***')
    print('Strzaly: {}'.format(boardUtils.get_shots_count()))
    print('Zestrzelone statki: {}'.format(boardUtils.get_score()))

if __name__ == '__main__':
    main()
