import random

class BoardUtils:
    size = 0
    def initBoard(self, size):
        self.size = size
        self.board = [['#' for x in range(size)] for y in range(size)]

    def drawBoard(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.board[y][x] + ' ', end='')
            print()
