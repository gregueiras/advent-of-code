from typing import List


class Instruction:
    def __init__(self, line: str) -> None:
        inst = line.split(" -> ")
        p1 = inst[0].split(",")
        self.x1 = int(p1[0])
        self.y1 = int(p1[1])

        p2 = inst[1].split(",")
        self.x2 = int(p2[0])
        self.y2 = int(p2[1])

    def isHorizontal(self) -> bool:
        return self.y1 == self.y2

    def isVertical(self) -> bool:
        return self.x1 == self.x2

    def isDiagonal(self) -> bool:
        return abs(self.x2 - self.x1) == abs(self.y2 - self.y1)

    def buildIntermediatePoints(self) -> List[List[int]]:
        res = []
        inc_x = 1 if self.x2 > self.x1 else -1
        inc_y = 1 if self.y2 > self.y1 else -1

        temp_x = self.x1
        temp_y = self.y1

        while temp_y != self.y2 and temp_x != self.x2:
            res.append([temp_x, temp_y])
            temp_x += inc_x
            temp_y += inc_y

        res.append([self.x2, self.y2])

        return res

    def __str__(self) -> str:
        return f"{self.x1}, {self.y1} -> {self.x2},{self.y2}"


class Board:
    def __init__(self, instructions: List[Instruction]) -> None:
        self.x_size = 1 + \
            max(map(lambda inst: max(inst.x1, inst.x2), instructions))
        self.y_size = 1 + \
            max(map(lambda inst: max(inst.y1, inst.y2), instructions))

        self.board = [0 for _ in range(self.x_size * self.y_size)]

    def play(self, instruction: Instruction) -> None:
        if instruction.isHorizontal():
            start = min(instruction.x1, instruction.x2)
            end = max(instruction.x1, instruction.x2)
            for inc in range(start, end + 1):
                self.board[instruction.y1 * self.x_size + inc] += 1

        elif instruction.isVertical():
            start = min(instruction.y1, instruction.y2)
            end = max(instruction.y1, instruction.y2)
            for inc in range(start, end + 1):
                self.board[instruction.x1 + (self.y_size * inc)] += 1

        elif instruction.isDiagonal():
            points = instruction.buildIntermediatePoints()
            for point in points:
                x = point[0]
                y = point[1]

                self.board[x + y * self.x_size] += 1

    def score(self, target: int) -> int:
        res = 0
        for n in self.board:
            res += int(n >= target)

        return res

    def __str__(self) -> str:
        res = ""

        idx = 0
        for _ in range(self.y_size):
            for __ in range(self.x_size):
                number = self.board[idx]
                res += str(number if number != 0 else ".").ljust(2)
                idx += 1
            res += "\n"

        return res
