from typing import List, Tuple
from math import floor


class Board:

    def __init__(self, dots: List[int], instructions: List[Tuple[str, int]]):
        self.dots = dots
        self.instructions = instructions

        self.dimX = max(list(map(lambda dot: dot[0], dots))) + 1
        self.dimY = max(list(map(lambda dot: dot[1], dots))) + 1

        self.board = [0 for _ in range(self.dimX * self.dimY)]

        for dot in dots:
            self.board[dot[0] + dot[1] * self.dimX] = 1

    def at(self, x, y):
        return self.board[self.atIdx(x, y)]

    def atIdx(self, x, y):
        return x + y * self.dimX

    def fold(self, instruction, debug=False):
        direction = instruction[0]
        pointer = instruction[1]

        if debug:
            new_board = self.board.copy()
            if direction == 'x':
                for idx in range(self.dimY):
                    new_board[pointer + idx * self.dimX] = '|'
            else:
                for idx in range(self.dimX):
                    new_board[idx + pointer * self.dimX] = '-'

            print(self._printBoard(new_board))

        if direction == 'y':
            oldDimY = self.dimY
            self.dimY = pointer
            newSize = self.dimX * self.dimY
            for idx in range(newSize):
                x = idx % self.dimX
                #y = oldDimY - (idx // self.dimX)
                y = pointer + (pointer - idx // self.dimX)
                self.board[idx] += self.at(x, y)

            self.board = self.board[:newSize]
        elif direction == 'x':
            newBoard = []
            for y in range(self.dimY):
                for x in range(pointer):
                    mergeX = self.dimX - x - 1
                    newBoard.append(self.at(x, y) + self.at(mergeX, y))

            self.dimX = pointer
            self.board = newBoard

        if debug:
            print(self._printBoard(self.board))

    def _printBoard(self, board):
        res = ''

        idx = 0
        for cell in board:
            if isinstance(cell, int) and cell == 0:
                res += '.'
            elif isinstance(cell, int) and cell > 0:
                res += '#'
            else:
                res += cell

            idx += 1
            if idx % self.dimX == 0:
                res += '\n'

        return res

    def __str__(self):
        return self._printBoard(self.board)

    def visible(self):
        newBoard = list(map(lambda val: 0 if val == 0 else 1, self.board))
        return sum(newBoard)
