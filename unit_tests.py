import pytest
from Board import Board
from Point import Point
from Shot import Shot
from ShipPart import ShipPart


def test_board_dim_x_equals10():
    dim_x = dim_y = 10
    board = Board(dim_x, dim_y)
    assert board.get_size_x() == dim_x


def test_board_dim_y_equals10():
    dim_x = dim_y = 10
    board = Board(dim_x, dim_y)
    assert board.get_size_y() == dim_y


def test_strike():
    dim_x = dim_y = 10
    board = Board(dim_x, dim_y)
    board.create()
    board.place_ship(Point(1, 1), 1, True)
    assert board.strike(Point(1, 1)) == Shot.SHOT_SUCCESSFUL


def test_is_free_place():
    dim_x = dim_y = 10
    board = Board(dim_x, dim_y)
    board.create()
    assert board.is_free_place(Point(0, 0), 4, True) is True


def test_ship_count_equals4():
    dim_x = dim_y = 10
    board = Board(dim_x, dim_y)
    board.create()
    board.rand_ship(4)
    assert ShipPart.counter == 4
