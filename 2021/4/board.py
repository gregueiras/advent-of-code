from typing import List, final
from collections.abc import Iterable


class Board:
    def __init__(self, numbers: List[List[str]]):
        self.size = len(numbers[0])
        self.numbers = numbers
        self.lastNumber = None
        self.gameEnded = False

    def play(self, number:str) -> bool:
        if self.gameEnded:
            return False

        self.markNumber(number)
        self.lastNumber = int(number)

        return self.hasWin();

    def hasWin(self) -> bool:
        res = self.hasCol() or self.hasRow() 
        self.gameEnded |= res

        return res 

    def hasRow(self) -> bool:
        for line in self.numbers:
            s = sum(map(lambda val : int(val), line))
            if s == 0:
                return True

        return False
    
    def hasCol(self) -> bool:
        cols = [[] for _ in self.numbers[0]]

        for line in self.numbers:
            for idx in range(len(line)):
                cols[idx].append(line[idx])

        for line in cols:
            s = sum(map(lambda val : int(val), line))
            if s == 0:
                return True

        return False

    def markNumber(self, number: str) -> None:
        for lineIdx in range(len(self.numbers)):
            for colIdx in range(len(self.numbers[lineIdx])):
                n = self.numbers[lineIdx][colIdx]
                if n == number:
                    self.numbers[lineIdx][colIdx] = 0
    

    def calcScore(self) -> int:
        allNumbers = flatten(self.numbers)
        allNumbers = map(lambda val : int(val), allNumbers)

        return self.lastNumber * sum(allNumbers)

    def __str__(self):
        finalStr = "";

        for line in self.numbers:
            for n in line:
                finalStr += str(n).rjust(2) + " "
            finalStr += "\n"

        return finalStr


def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el
