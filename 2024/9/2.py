import dis
from mmap import ACCESS_WRITE
import os

from tqdm import tqdm

PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def every(arr, target):
    return all(map(lambda x: x == target, arr))


def clean_acc(acc):
    new_acc = []

    for i in range(len(acc)):
        pos = acc[i]
        if every(pos, "."):
            if every(new_acc[-1], "."):
                new_acc[-1] = new_acc[-1] + pos
            else:
                new_acc.append(pos)
        else:
            new_acc.append(pos)

    return new_acc


with open(PATH) as file_in:
    puzzle = []

    for line in file_in:
        try:
            line = line.strip()
            puzzle = list(map(int, line))
        except ValueError:
            pass

    acc = []

    is_empty_space = False
    id = 0

    for i in puzzle:
        if is_empty_space and i != 0:
            acc.append(["." for _ in range(i)])
        elif i != 0:
            acc.append([str(id) for _ in range(i)])

        if not is_empty_space:
            id += 1
        is_empty_space = not is_empty_space

    with tqdm(total=len(acc), disable=False) as pbar:
        for right_idx in range(len(acc) - 1, 0, -1):
            pbar.update()
            pbar.refresh()

            right = acc[right_idx]

            if right[0] != ".":
                len_right = len(right)

                for left_idx in range(0, right_idx):
                    left = acc[left_idx]
                    len_left = len(left)

                    if left[0] == "." and len_left >= len_right:
                        acc[left_idx] = right

                        """ if right_idx + 1 < len(acc) and (every(acc[right_idx + 1], ".")):
                            acc[right_idx] = ["." for _ in range(len_right)]
                            acc[right_idx].extend(acc[right_idx + 1])
                            del acc[right_idx + 1]
                        else: """
                        acc[right_idx] = ["." for _ in range(len_right)]

                        

                        if (len_left - len_right) > 0:
                            if every(acc[left_idx + 1], "."):
                                acc[left_idx + 1] = [
                                    "."
                                    for _ in range(
                                        len_left - len_right + len(acc[left_idx + 1])
                                    )
                                ]
                            else:
                                acc.insert(
                                    left_idx + 1,
                                    ["." for _ in range(len_left - len_right)],
                                )

                        break
                    #print(acc)

                    acc = clean_acc(acc)

    print(acc)
    acc = [item for sublist in acc for item in sublist]

    sum_acc = 0
    for idx in range(len(acc)):
        if acc[idx] != ".":
            sum_acc += int(acc[idx]) * idx

    print(sum_acc)
