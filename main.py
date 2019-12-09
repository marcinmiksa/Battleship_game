# TODO: Czyszczenie ekranu
import utils

boardUtils = utils.BoardUtils()

print("Podaj rozmiar planszy: ")
size = int(input())
print("Podaj rozmiar planszy: ")

boardUtils.init_board(size)
boardUtils.draw_board()
