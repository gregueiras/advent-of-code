import os
from aux import Graph

PATH =  os.path.join(os.path.dirname(__file__), 'test_input.txt')

with open(PATH) as file_in:
    lines: "list[str]" = []
    for line in file_in:
        l = line.strip('\n')
        lines.append(l)

graph = Graph(lines)

graph.explore()