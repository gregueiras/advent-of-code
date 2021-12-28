import os
PATH =  os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        lines.append(line)

x = 0
y = 0
aim = 0

for line in lines:
    [inst, size] = line.split(" ")
    size = int(size)

    if inst == "forward":
        x += size
        y += aim * size
    elif inst == "down":
        aim += size
    elif inst == "up":
        aim -= size

    print(f"X: {x}\tY: {y}\tAim: {aim}")
    
    

print(f"X: {x}\tY: {y}")
print(x * y)