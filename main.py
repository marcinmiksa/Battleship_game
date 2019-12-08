# TODO: Czyszczenie ekranu
import utils
import Ship as ship
import Point as pt

boardUtils = utils.BoardUtils()

print("Podaj rozmiar planszy: ")
size = int(input())

boardUtils.initBoard(size)
boardUtils.drawBoard()
