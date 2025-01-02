from ast import Dict
from hmac import new
from typing import List
import os
from pprint import pprint
from math import floor, log10
from tqdm import tqdm

PATH = os.path.join(os.path.dirname(__file__), "input.txt")

# cache = {}


def blink(stones: dict[int, int]) -> dict[int, int]:
    new_stones = {}

    for stone, freq in stones.items():
        if not stone:
            new_stones[1] = new_stones.get(1, 0) + freq
        elif not len(str(stone)) % 2:
            middle = len(str(stone)) // 2
            first_half = int(str(stone)[middle:])
            second_half = int(str(stone)[:middle])

            new_stones[first_half] = new_stones.get(first_half, 0) + freq
            new_stones[second_half] = new_stones.get(second_half, 0) + freq
        else:
            new_stones[stone * 2024] = new_stones.get(stone * 2024, 0) + freq

    return new_stones


with open(PATH) as file_in:
    stones = {}

    for line in file_in:
        try:
            line = line.strip()
            new_stones = list(map(int, line.split(" ")))
            for stone in new_stones:
                if stone in stones:
                    stones[stone] += 1
                else:
                    stones[stone] = 1

        except ValueError:
            pass

    print(stones)

    with tqdm(total=75, disable=False) as pbar:
        for _ in range(75):
            stones = blink(stones)
            pbar.update()
            pbar.refresh()

    print(sum(stones.values()))
