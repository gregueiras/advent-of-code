import os
PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

size = len(lines[0])

o2 = 0
co2 = 0

bit_idx = 0
acc = 0

orig_lines = lines

while len(lines) > 1:
    for line in lines:
        acc += int(line[bit_idx])

    most_common = int(acc >= len(lines) / 2)
    new_lines = []
    for l in lines:
        if int(l[bit_idx]) == most_common:
            new_lines.append(l)

    lines = new_lines
    acc = 0
    bit_idx += 1

for idx in range(size - 1, -1, -1):
    exp = size - idx - 1
    if lines[0][idx] == '1':
        o2 += pow(2, exp)


lines = orig_lines
bit_idx = 0
acc = 0

while len(lines) > 1:
    for line in lines:
        acc += int(line[bit_idx])

    most_common = int(acc < len(lines) / 2)
    new_lines = []
    for l in lines:
        if int(l[bit_idx]) == most_common:
            new_lines.append(l)

    lines = new_lines
    acc = 0
    bit_idx += 1

for idx in range(size - 1, -1, -1):
    exp = size - idx - 1
    if lines[0][idx] == '1':
        co2 += pow(2, exp)

print(f"O2: {o2}\tCO2: {co2}")
print(o2 * co2)