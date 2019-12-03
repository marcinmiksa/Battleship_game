# TODO: Czyszczenie ekranu
import utils

boardUtils = utils.BoardUtils()

print("Podaj rozmiar planszy: ")
size = int(input())

boardUtils.initBoard(size)
boardUtils.drawBoard()


