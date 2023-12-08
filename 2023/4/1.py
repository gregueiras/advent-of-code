from operator import is_
from pprint import pprint
import os
from typing import Dict, List, Set, Tuple

PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Game:
    def __init__(self, line: str) -> None:
        splitColon = line.split(": ")

        self.id = splitColon[0].split(" ")[1]

        splitLine = splitColon[1].split(" | ")

        self.winningNumbers: Set[int] = set(map(int, splitLine[0].split()))
        self.cardNumbers: Set[int] = set(map(int, splitLine[1].split()))

    def evaluate(self) -> int:
        intersection = len(self.winningNumbers.intersection(self.cardNumbers))

        if intersection == 0:
            return 0

        return pow(2, intersection - 1)


games: List[Game] = []

with open(PATH) as file_in:
    for line in file_in:
        try:
            games.append(Game(line.strip()))
        except ValueError:
            pass

acc = 0
for game in games:
    acc += game.evaluate()

print(acc)
