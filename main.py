# TODO: Czyszczenie ekranu
import utils



print("Podaj rozmiar planszy: ")
size = int(input())
print("Podaj rozmiar planszy: ")

boardUtils = utils.BoardUtils(size)
boardUtils.draw_board()
