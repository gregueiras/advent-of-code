from functools import reduce
from operator import is_
import operator
from pprint import pprint
import os
from typing import Dict, List, Tuple

PATH = os.path.join(os.path.dirname(__file__), "input.txt")


class Number:
    def __init__(
        self,
        init_x: int,
        end_x: int,
        y: int,
        value: int,
    ) -> None:
        self.init_x = init_x
        self.end_x = end_x
        self.y = y
        self.value = value

    def __str__(self) -> str:
        return f"FOUND: {self.value} -> {self.init_x},{self.end_x} ->  {self.y}"

    def __repr__(self) -> str:
        return self.__str__()
    
def is_neighbor(numbers: List[Number], symbol: Tuple[int, int]) -> int:
        neighbor_numbers: List[Number] = []
        
        for number in numbers:
            sym_x, sym_y = symbol

            is_vertical = number.y - 1 <= sym_y <= number.y + 1
            is_horizontal = number.init_x - 1 <= sym_x <= number.end_x + 1

            if is_vertical and is_horizontal:
                neighbor_numbers.append(number)

        if len(neighbor_numbers) < 2:
            return 0

        return reduce(operator.mul, map(lambda n: n.value, neighbor_numbers))

class Board:
    def __init__(self, board: List[List[str]]) -> None:
        self.board = board

        self.numbers: List[Number] = []
        self.symbols: List[Tuple[int, int]] = []

        y = 0
        for line in board:
            x = 0
            acc = ""
            for x in range(len(line) - 1, -2, -1):
                character = line[x]

                #if character in {'*', '+', '$', '#', '%', '-', '&', '/', '@', '='}:
                if not isInt(character) and character == "*":
                    self.symbols.append((x, y))

                if not isInt(character) and acc != "":
                    self.numbers.append(
                        Number(
                            x + 1,
                            x + len(str(acc)),
                            y,
                            int(acc),
                        ),
                    )
                    acc = ""
                elif isInt(character):
                    value = str(character)
                    acc = value + acc

            y += 1


def isInt(num: str):
    try:
        int(num)
        return True
    except:
        return False


board: List[List[str]] = []

with open(PATH) as file_in:
    for line in file_in:
        try:
            board.append(list(line.strip()))
        except ValueError:
            pass

acc = 0

for line in board:
    print(line)

game_board = Board(board)

pprint(game_board.numbers)
#pprint(game_board.symbols)

acc = 0
for symbol in game_board.symbols:
    acc += is_neighbor(game_board.numbers, symbol)

print(acc)