from typing import List, Union


class Board:
    def __init__(self, board: List[List[int]]) -> None:
        self.len = len(board[0])

        self.board: List[int] = list(map(int, flatten(board)))
        self.flashes = 0

    def _up(self, index: int) -> Union[int, None]:
        idx = index - self.len

        if idx < 0:
            return None

        return idx

    def _down(self, index: int) -> Union[int, None]:
        idx = index + self.len

        if idx >= len(self.board):
            return None
        else:
            return idx

    def _left(self, index: int) -> Union[int, None]:
        if (index % self.len) == 0:
            return None
        else:
            return index - 1

    def _right(self, index: int) -> Union[int, None]:
        if (index % self.len) == self.len - 1:
            return None
        else:
            return index + 1

    def _right_up(self, index: int) -> Union[int, None]:
        idx = index - self.len

        if idx < 0 or (index % self.len) == self.len - 1:
            return None
        else:
            return idx + 1

    def _right_down(self, index: int) -> Union[int, None]:
        idx = index + self.len

        if (index % self.len) == self.len - 1 or idx + 1 >= len(self.board):
            return None
        else:
            return idx + 1

    def _left_up(self, index: int) -> Union[int, None]:
        idx = index - self.len

        if idx < 0 or (index % self.len) == 0:
            return None
        else:
            return idx - 1

    def _left_down(self, index: int) -> Union[int, None]:
        idx = index + self.len

        if (index % self.len) == 0 or idx >= len(self.board):
            return None
        else:
            return idx - 1

    def neighbors(self, idx):
        return [
            self._up(idx),
            self._right_up(idx),
            self._right(idx),
            self._right_down(idx),
            self._down(idx),
            self._left_down(idx),
            self._left(idx),
            self._left_up(idx),
        ]

    def _flash(self, idx: int):
        neighbors = self.neighbors(idx)
        self.board[idx] = None
        self.flashes += 1

        for neighbor in neighbors:
            if neighbor is None or self.board[neighbor] is None:
                continue
            
            self.board[neighbor] += 1
            if self.board[neighbor] is not None and self.board[neighbor] > 9:
                self._flash(neighbor)
        

    def _step(self):
        self.board = list(map(lambda octopus: octopus + 1, self.board))

        for idx in range(len(self.board)):
            octopus = self.board[idx]
            if octopus is not None and octopus > 9:
                self._flash(idx)

        self.board = list(map(lambda octopus: octopus if octopus is not None else 0, self.board))


    def steps(self, n):
        for _ in range(n):
            self._step()

    def findSyncronizing(self) -> int:
        for n in range(int(1e5)):
            self._step()

            if sum(self.board) == 0:
                return n


    def __str__(self) -> str:
        ret = ""
        for i in range(len(self.board)):
            val = self.board[i]

            ret += str(val)
            if i % self.len == self.len - 1:
                ret += "\n"

        return ret


def flatten(L: List[List[int]]) -> List[int]:
    return [item for sublist in L for item in sublist]
