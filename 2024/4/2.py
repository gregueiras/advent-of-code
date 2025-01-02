from hmac import new
import os

PATH = os.path.join(os.path.dirname(__file__), "input.txt")
target_word = "MAS"
reverse_target_word = "".join(list(reversed(target_word)))


def cross(lines, x, y):
    if x + 2 > max_x or y + 2 > max_y:
        return 0

    l1 = lines[y][x]
    l2 = lines[y + 1][x + 1]
    l3 = lines[y + 2][x + 2]

    r1 = lines[y][x + 2]
    r2 = lines[y + 1][x + 1]
    r3 = lines[y + 2][x]

    l_word = l1 + l2 + l3
    r_word = r1 + r2 + r3

    l_match = l_word == target_word or l_word == reverse_target_word
    r_match = r_word == target_word or r_word == reverse_target_word

    if l_match and r_match:
        solution[y][x] = l1
        solution[y + 1][x + 1] = l2
        solution[y + 2][x + 2] = l3

        solution[y][x + 2] = r1
        solution[y + 1][x + 1] = r2
        solution[y + 2][x] = r3

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
                    cross(lines, x, y),
                ]

                acc += sum(options)
            except:
                print(f"ERROR {x} {y}")

    #for line in solution:
    #    print("".join(line))

    print()

    print(acc)
