import os
from aux import Reactor

PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

reactor = Reactor()

for line in lines:
    reactor.instruction(line)
    print(len(reactor.cubes))