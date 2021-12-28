import os
PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines = []
    for line in file_in:
        lines.append(int(line))


counter = 0;

is_first_line = True
previous_measure = None


for measure in lines:
  if is_first_line:
    is_first_line = False
    previous_measure = measure
    continue

  if measure > previous_measure:
    counter += 1

  previous_measure = measure


print(counter)
