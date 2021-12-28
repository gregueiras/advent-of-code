import os
PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

size = len(lines[0])

acc = [0 for x in range(size)]

for line in lines:
    for idx in range(size - 1, -1, -1):
        acc[idx] += int(line[idx])

gamma = 0
epsilon = 0
for idx in range(size - 1, -1, -1):
    exp = size - idx - 1
    if acc[idx] > len(lines) / 2:
        gamma += pow(2, exp)
    else:
        epsilon += pow(2, exp)
    acc[idx] = int(acc[idx] > len(lines) / 2)


print(acc)
print(f"Gamma: {gamma}\tEpsilon: {epsilon}")
print(gamma * epsilon)