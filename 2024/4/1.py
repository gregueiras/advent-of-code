from hmac import new
import os

PATH = os.path.join(os.path.dirname(__file__), "input.txt")
target_word = "XMAS"
reverse_target_word = "".join(list(reversed(target_word)))


def vertical(lines, x, y):
    if y + 3 > max_y:
        return 0

    l1 = lines[y][x]
    l2 = lines[y + 1][x]
    l3 = lines[y + 2][x]
    l4 = lines[y + 3][x]

    word = l1 + l2 + l3 + l4

    if word == target_word or word == reverse_target_word:
        solution[y][x] = l1
        solution[y + 1][x] = l2
        solution[y + 2][x] = l3
        solution[y + 3][x] = l4
        return 1

    return 0


def horizontal(lines, x, y):
    if x + 3 > max_x:
        return 0

    l1 = lines[y][x]
    l2 = lines[y][x + 1]
    l3 = lines[y][x + 2]
    l4 = lines[y][x + 3]

    word = l1 + l2 + l3 + l4

    if word == target_word or word == reverse_target_word:
        solution[y][x] = l1
        solution[y][x + 1] = l2
        solution[y][x + 2] = l3
        solution[y][x + 3] = l4
        return 1

    return 0


def diagonal_left(lines, x, y):
    if x - 3 < 0 or y + 3 > max_y:
        return 0

    l1 = lines[y][x]
    l2 = lines[y + 1][x - 1]
    l3 = lines[y + 2][x - 2]
    l4 = lines[y + 3][x - 3]

    word = l1 + l2 + l3 + l4

    if word == target_word or word == reverse_target_word:
        solution[y][x] = l1
        solution[y + 1][x - 1] = l2
        solution[y + 2][x - 2] = l3
        solution[y + 3][x - 3] = l4
        return 1

    return 0


def diagonal_right(lines, x, y):
    if x + 3 > max_x or y + 3 > max_y:
        return 0

    l1 = lines[y][x]
    l2 = lines[y + 1][x + 1]
    l3 = lines[y + 2][x + 2]
    l4 = lines[y + 3][x + 3]

    word = l1 + l2 + l3 + l4

    if word == target_word or word == reverse_target_word:
        solution[y][x] = l1
        solution[y + 1][x + 1] = l2
        solution[y + 2][x + 2] = l3
        solution[y + 3][x + 3] = l4
        return 1

    return 0


with open(PATH) as file_in:
    lines = []

    for line in file_in:
        try:
            lines.append(list(line.strip()))
        except ValueError:
            pass

    for line in lines:
        print(line)

    print()
    solution = []
    for y in range(len(lines)):
        new_line = []
        for x in range(len(lines[0])):
            new_line.append(".")
        solution.append(new_line)

    max_x = len(lines[0]) - 1
    max_y = len(lines) - 1

    acc = 0
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            try:
                options = [
                    vertical(lines, x, y),
                    horizontal(lines, x, y),
                    diagonal_left(lines, x, y),
                    diagonal_right(lines, x, y),
                ]

                acc += sum(options)
            except:
                print(f"ERROR {x} {y}")

    #for line in solution:
    #    print("".join(line))

    print()

    print(acc)
