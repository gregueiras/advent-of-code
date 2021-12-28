from os import error
from typing import List, Set


class Display:
    def __init__(self) -> None:
        self.zero = set()
        self.one = set()
        self.two = set()
        self.three = set()
        self.four = set()
        self.five = set()
        self.six = set()
        self.seven = set()
        self.eight = set()
        self.nine = set()

    def empty(self, digits):
        return len(digits) == 0


    def tryGuess(self, digits: Set):        
        emptyEasy = self.empty(self.one) or self.empty(self.four) or self.empty(self.seven)

        if (not emptyEasy) and self.empty(self.nine):
            matches = digits.issuperset(self.four) and digits.issuperset(self.seven.difference(self.one))

            if matches:
                self.nine = digits
        elif not (self.empty(self.nine)) and len(digits) == 6:
            if digits.issuperset(self.one) and self.empty(self.zero):
                self.zero = digits
            elif self.empty(self.six):
                self.six = digits
        elif not (self.empty(self.nine) or self.empty(self.six)) and self.empty(self.five):
            matches = self.six.difference(digits) == self.eight.difference(self.nine)

            if matches:
                self.five = digits
        elif not (self.empty(self.nine) or self.empty(self.six) or self.empty(self.five)) and len(digits) == 5:
            if digits.issuperset(self.one) and self.empty(self.three):
                self.three = digits
            elif self.empty(self.two):
                self.two = digits

    def guess(self, digits: List[str]):

        digitsSet = set(digits)
        size = len(digits)
        if size == 2:
            self.one = digitsSet
        elif size == 3:
            self.seven = digitsSet
        elif size == 4:
            self.four = digitsSet
        elif size == 7:
            self.eight = digitsSet
        else:
            self.tryGuess(digitsSet)

    def translate(self, number: List[str]):
        numberSet = set(number)

        if self.zero == numberSet:
            return 0
        elif self.one == numberSet:
            return 1
        elif self.two == numberSet:
            return 2
        elif self.three == numberSet:
            return 3
        elif self.four == numberSet:
            return 4
        elif self.five == numberSet:
            return 5
        elif self.six == numberSet:
            return 6
        elif self.seven == numberSet:
            return 7
        elif self.eight == numberSet:
            return 8
        elif self.nine == numberSet:
            return 9
        else:
            raise Exception("Ups!")


    def calcOutput(self, output: List[List[str]]):
        acc = 0
        
        for exp, number in zip(range(3, -1, -1), output):
            acc += self.translate(number) * pow(10, exp)

        return acc


    def finished(self):
        return not(self.empty(self.zero) or self.empty(self.one) or self.empty(self.two) or self.empty(self.three) or self.empty(self.four) or self.empty(self.five) or self.empty(self.six) or self.empty(self.seven) or self.empty(self.eight) or self.empty(self.nine))