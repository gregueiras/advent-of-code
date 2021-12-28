import networkx as nx
import matplotlib.pyplot as plt

from numpy import loadtxt

instructions = loadtxt("./input.txt", delimiter="\n", unpack=False, dtype=str)

G = nx.Graph()


def processLine(line):
    orig, dest = line.split(")")

    if (orig not in G):
        G.add_node(orig)

    if (dest not in G):
        G.add_node(dest)

    G.add_edge(orig, dest)
    G.add_edge(dest, orig)


for inst in instructions:
    processLine(inst)


path = nx.shortest_path(G, "YOU", "SAN")
distance = len(path)
print(path, "\t", distance - 3)

nx.draw(G)

plt.show()
