from typing import List, Union


class Board:
    def __init__(self, board: List[List[int]]) -> None:
        self.len = len(board[0])

        self.board: List[int] = list(map(int, flatten(board)))

    def _up(self, index: int) -> Union[int, None]:
        idx = index - self.len

        if idx < 0:
            return None

        try:
            return self.board[idx]
        except IndexError:
            return None

    def _down(self, index: int) -> Union[int, None]:
        try:
            return self.board[index + self.len]
        except IndexError:
            return None

    def _left(self, index: int) -> Union[int, None]:
        if (index % self.len) == 0:
            return None
        else:
            return self.board[index - 1]

    def _right(self, index: int) -> Union[int, None]:
        if (index % self.len) == self.len - 1:
            return None
        else:
            return self.board[index + 1]

    def _isLow(self, index: int) -> bool:
        near = [
            self._up(index),
            self._right(index),
            self._down(index),
            self._left(index),
        ]

        point = self.board[index]
        for neighbour in near:
            if neighbour != None and point >= neighbour:
                return False

        return True

    def findLow(self) -> List[int]:
        acc = []
        for i in range(len(self.board)):
            if self._isLow(i):
                acc.append(self.board[i])

        return acc

    def findLowIdx(self) -> List[int]:
        acc = []
        for i in range(len(self.board)):
            if self._isLow(i):
                acc.append(i)

        return acc

    def _exploreBasin(self, index):
        options = [
            self._up(index),
            self._right(index),
            self._down(index),
            self._left(index),
        ]
        incs = [
            -self.len,
            1,
            self.len,
            -1
        ]

        acc = []

        point = self.board[index]
        for neighbour, inc in zip(options, incs):
            if neighbour != None and neighbour != 9 and neighbour > point:
                acc.extend([index + inc])
                acc.extend(self._exploreBasin(index + inc))

        return acc

    def findBasin(self):
        acc = []
        lowPoints = self.findLowIdx()

        for i in lowPoints:
            temp = self._exploreBasin(i)
            temp.append(i)
            acc.append(list(set(temp)))

        return acc


def flatten(L: List[List[int]]) -> List[int]:
    return [item for sublist in L for item in sublist]
