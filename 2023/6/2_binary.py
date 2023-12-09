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

        midPoint:int = self.time // 2
        leftMidPoint:int = midPoint // 2
        step:int = leftMidPoint

        #leftSearch
        stopSearch = False
        leftBreak = 0

        if (self._distanceReached(midPoint) > self.distance):
          while stopSearch != True:
            hasReached = self._distanceReached(leftMidPoint) > self.distance
            leftNeighborHasReached = self._distanceReached(leftMidPoint - 1) > self.distance

            if (hasReached and not leftNeighborHasReached):
                stopSearch = True
                leftBreak = leftMidPoint

            factor = -1 if hasReached else 1
            leftMidPoint = factor * step // 2 + leftMidPoint
            step = step // 2

        print(leftBreak)
        return self.time - leftBreak * 2 + 1

        """ for holdTime in range(1, self.time):
            distanceReached = self._distanceReached(holdTime)
            

            if distanceReached > self.distance:
                accWin += 1 

        return accWin"""

        """ return sum(res) """


race: Race

with open(PATH) as file_in:
    lines = file_in.readlines()
    time = int("".join(lines[0].split(":")[1].split()))
    distance = int("".join(lines[1].split(":")[1].split()))

    race = Race(time, distance)


print(race.evaluate())
