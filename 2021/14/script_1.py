from pathlib import Path

path = Path(__file__).parent / "./input.txt"

template = []
instructions = {}


idx = 0
with open(path) as fp:
    Lines = fp.readlines()
    for line in Lines:
        line = line.strip()
        if line == "":
            continue
        if idx == 0:
            template = list(line)
        else:
            temp = line.split(" -> ")
            instructions[temp[0]] = temp[1]

        idx += 1


print(f"Template:     {''.join(template)}")

chains = {}
for i in range(len(template) - 1):
    key = template[i] + template[i + 1]
    if key in chains.keys():
        chains[key] += 1
    else:
        chains[key] = 1

for i in range(40):
    new_count = dict.fromkeys(instructions.keys(), 0)
    for pair, value in chains.items():
        if value == 0:
            continue
        new = instructions[pair]
        new_count[pair[0] + new] += value
        new_count[new + pair[1]] += value

    chains = new_count


letters = {}
for pair, value in chains.items():
    if pair[0] in letters.keys():
        letters[pair[0]] += value
    else:
        letters[pair[0]] = value

lastLetter = template[-1]
if lastLetter in letters.keys():
    letters[lastLetter] += 1
else:
    letters[lastLetter] = 1

maxV = max(letters.values())
minV = min(letters.values())

print(maxV)
print(minV)
print(maxV - minV)
