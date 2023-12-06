import os
from typing import Dict, List

PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Game:
    def __init__(self, line: str):
        colonSplit = line.split(": ")

        self.id: int = int(colonSplit[0].split(" ")[1])

        sets = colonSplit[1].split("; ")

        self.gameSets: List[Dict[str, int]] = []

        for gameSet in sets:
            thisSet = {}
            cubes = gameSet.split(", ")

            for cube in cubes:
                cubeSplit = cube.split(" ")
                thisSet[cubeSplit[1].strip()] = int(cubeSplit[0])

            self.gameSets.append(thisSet)

    def validate(self, rules: Dict[str, int]) -> bool:
        for gameSet in self.gameSets:
            for color, value in gameSet.items():
                if value > rules[color]:
                    return False

        return True


with open(PATH) as file_in:
    games: List[Game] = []
    for line in file_in:
        try:
            games.append(Game(line))
        except ValueError:
            pass

rules = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
acc = 0

for game in games:
    isValid = game.validate(rules)

    acc += game.id if isValid else 0

print(acc)
