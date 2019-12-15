# TODO: Czyszczenie ekranu
import utils


print("Podaj wymiar planszy w poziomie: ")
board_dimensions_x = int(input())
print("Podaj wymiar planszy w pionie: ")
board_dimensions_y = int(input())

boardUtils = utils.BoardUtils(board_dimensions_x, board_dimensions_y)
boardUtils.draw_board()
