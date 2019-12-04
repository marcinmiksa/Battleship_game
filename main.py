# TODO: Czyszczenie ekranu
import utils
import Ship as ship
import Point as pt

boardUtils = utils.BoardUtils()

print("Podaj rozmiar planszy: ")
size = int(input())

boardUtils.initBoard(size)
boardUtils.drawBoard()

point = pt.Point(2, 2)
ship = ship.Ship(point, 3)
print(ship.getCoordinates())

