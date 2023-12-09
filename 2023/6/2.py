import dis
from functools import reduce
from operator import is_
import operator
from pprint import pprint
import os
from typing import Dict, List, Set, Tuple

PATH = os.path.join(os.path.dirname(__file__), "test_input.txt")


class Race:
    def __init__(self, time: int, distance: int) -> None:
        self.time = time
        self.distance = distance

    def _distanceReached(self, speed: int):
        return (self.time - speed) * speed

    def evaluate(self) -> int:
        accWin = 0

        for holdTime in range(1, self.time):
            distanceReached = self._distanceReached(holdTime)
            print(f"{str(holdTime).zfill(8)}/{self.time} -> {distanceReached}", end="\r")

            if distanceReached > self.distance:
                accWin += 1

        return accWin


race: Race

with open(PATH) as file_in:
    lines = file_in.readlines()
    time = int("".join(lines[0].split(":")[1].split()))
    distance = int("".join(lines[1].split(":")[1].split()))

    race = Race(time, distance)


print(race.evaluate())
