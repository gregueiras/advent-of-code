import os
PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines = []
    for line in file_in:
        lines.append(int(line))


counter = 0;

is_first_line = True
previous_measure = None


for idx in range(0, len(lines) - 2):
    if is_first_line:
        is_first_line = False
        previous_measure = lines[idx] + lines[idx + 1] + lines[idx + 2]
        continue

    sum_measure = lines[idx] + lines[idx + 1] + lines[idx + 2]

    if sum_measure > previous_measure:
     counter += 1

    previous_measure = sum_measure


print(counter)
