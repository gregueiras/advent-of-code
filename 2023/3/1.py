from operator import is_
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

    def is_neighbor(self, symbols: List[Tuple[int, int]]) -> bool:
        for symbol in symbols:
            sym_x, sym_y = symbol

            is_vertical = self.y - 1 <= sym_y <= self.y + 1
            is_horizontal = self.init_x - 1 <= sym_x <= self.end_x + 1

            if is_vertical and is_horizontal:
                return True

        return False

    def __str__(self) -> str:
        return f"FOUND: {self.value} -> {self.init_x},{self.end_x} ->  {self.y}"

    def __repr__(self) -> str:
        return self.__str__()

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
                if not isInt(character) and character != ".":
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
                    
                    #acc = value if acc == 0 else acc + value * pow(10, len(str(acc)))

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
for number in game_board.numbers:
    acc += number.value if number.is_neighbor(game_board.symbols) else 0

print(acc)