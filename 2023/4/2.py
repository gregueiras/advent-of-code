from functools import reduce
from operator import is_
import operator
from pprint import pprint
import os
from typing import Dict, List, Set, Tuple

PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Game:
    def __init__(self, line: str) -> None:
        splitColon = line.split(": ")

        self.id = int(splitColon[0].split()[1])

        splitLine = splitColon[1].split(" | ")

        self.winningNumbers: Set[int] = set(map(int, splitLine[0].split()))
        self.cardNumbers: Set[int] = set(map(int, splitLine[1].split()))

    def evaluate(self) -> int:
        intersection = len(self.winningNumbers.intersection(self.cardNumbers))

        return intersection


games: List[Game] = []

with open(PATH) as file_in:
    for line in file_in:
        try:
            games.append(Game(line.strip()))
        except ValueError:
            pass

acc = 0
wonCopies: Dict[int, int] = {}

for game in games:
    wonCopies[game.id] = 1

for id in wonCopies.keys():
    nextCopies = games[id - 1].evaluate()
    for idx in range(id, id + nextCopies):
        wonCopies[idx + 1] += wonCopies[id]

    print(wonCopies)

print("------\n\n")

print(wonCopies)
print(reduce(operator.add, wonCopies.values()))
