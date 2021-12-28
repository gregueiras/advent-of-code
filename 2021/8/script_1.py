import os

PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)


inputs = []
outputs = []
for line in lines:
    temp = line.split(" | ")
    
    inp = temp[0].split(" ")
    out = temp[1].split(" ")

    inputs.append(inp)
    outputs.append(out)

acc = 0
for out in outputs:
    for digit in out:
        if len(digit) in [2, 3, 4, 7]:
            acc += 1

print(acc)