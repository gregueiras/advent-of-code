from hmac import new
from typing import List
import os
from pprint import pprint
from math import floor, log10

PATH = os.path.join(os.path.dirname(__file__), "input.txt")

def blink(stones: List[int]) -> List[int]:
    new_stones = []
    
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            middle = len(str(stone)) // 2
            first_half = str(stone)[:middle]
            second_half = str(stone)[middle:]

            new_stones.append(int(first_half))
            new_stones.append(int(second_half))
        else:
            new_stones.append(stone * 2024)

    return new_stones

with open(PATH) as file_in:
    stones = []

    for line in file_in:
        try:
            line = line.strip()
            stones = list(map(int, line.split(" ")))
        except ValueError:
            pass

    print(stones)


    for _ in range(25):
        stones = blink(stones)

    print(len(stones))