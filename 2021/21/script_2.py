import os
from track import Track

PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

players = [int(l.split(": ")[1]) for l in lines]

universes = {}

def recur(turn, p1, p2, s1, s2):
    key = ' '.join(map(str, [turn, p1, p2, s1, s2]))

    if key in universes:
        return universes[key]

    if s1 >= 21:
        return [1, 0]
    if s2 >= 21:
        return [0, 1]

    ans = [0, 0]

    if turn == 1:
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    new_p1 = (p1 + i + j + k - 1) % 10 + 1
                    new_s1 = s1 + new_p1

                    res = recur(2, new_p1, p2, new_s1, s2)
                    ans[0] += res[0]
                    ans[1] += res[1]
    else:
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    new_p2 = (p2 + i + j + k - 1) % 10 + 1
                    new_s2 = s2 + new_p2

                    res = recur(1, p1, new_p2, s1, new_s2)
                    ans[0] += res[0]
                    ans[1] += res[1]

        universes[key] = ans
    return ans

print(max(recur(1, players[0], players[1], 0, 0)))
