import dis
from functools import reduce
from operator import is_
import operator
from pprint import pprint
import os
from typing import Dict, List, Set, Tuple

PATH = os.path.join(os.path.dirname(__file__), "input.txt")


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

            if distanceReached > self.distance:
                accWin += 1

        return accWin


races: List[Race] = []

with open(PATH) as file_in:
    lines = file_in.readlines()
    times = map(int, lines[0].split(":")[1].split())
    distances = map(int, lines[1].split(":")[1].split())

    for time, distance in zip(times, distances):
        races.append(Race(time, distance))
        break


print(reduce(operator.mul, map(lambda x: x.evaluate(), races)))
