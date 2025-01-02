from operator import is_
import os

from tqdm import tqdm

PATH = os.path.join(os.path.dirname(__file__), "input.txt")

def every(arr):
    return all(map(lambda x: x == arr[0], arr))

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
        for _ in range(i):
            if is_empty_space:
                acc.append(".")
            else:
                acc.append(str(id))


        if not is_empty_space:
            id += 1
        is_empty_space = not is_empty_space

    print("".join(acc))

    with tqdm(total=len(acc)) as pbar:
        for left_idx in range(len(acc)):
            pbar.update()
            pbar.refresh()
            
            left = acc[left_idx]

            if left == ".":
                for right_idx in range(len(acc) - 1, left_idx, -1):
                    right = acc[right_idx]

                    if right != ".":
                        acc[left_idx] = right
                        acc[right_idx] = left
                        break

            if every(acc[left_idx:]):
                break
        
        #print(f"{left_idx} -> {''.join(acc)}" )

    sum_acc = 0

    for idx in range(len(acc)):
        if acc[idx] != ".":
            sum_acc += int(acc[idx]) * idx


    print(sum_acc)