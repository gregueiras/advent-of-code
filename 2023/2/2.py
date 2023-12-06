from functools import reduce
import operator
import os
from typing import Dict, List

PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Game:
    def __init__(self, line: str):
        colonSplit = line.split(": ")

        self.id: int = int(colonSplit[0].split(" ")[1])

        sets = colonSplit[1].split("; ")

        self.cubeRecords: Dict[str, int] = {}

        for gameSet in sets:
            thisSet = {}
            cubes = gameSet.split(", ")

            for cube in cubes:
                cubeSplit = cube.split(" ")
                color = cubeSplit[1].strip()
                value = int(cubeSplit[0])

                if color in self.cubeRecords.keys():
                    if value > self.cubeRecords[color]:
                        self.cubeRecords[color] = value
                else:
                    self.cubeRecords[color] = value

            self.power = reduce(operator.mul, self.cubeRecords.values())


with open(PATH) as file_in:
    games: List[Game] = []
    for line in file_in:
        try:
            games.append(Game(line))
        except ValueError:
            pass

acc = 0

for game in games:
    acc += game.power

print(acc)
