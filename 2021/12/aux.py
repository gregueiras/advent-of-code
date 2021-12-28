from typing import List

class Node:
    def __init__(self, name: str) -> None:
        self.name = name

        self.isBig = name.upper() == name

    def __str__(self) -> str:
        return self.name

class Edge:
    def __init__(self, start: Node, end: Node) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f"{self.start}->{self.end}" 


class Graph:
    def __init__(self, lines: List[List[str]]) -> None:
        self.edges: List[Edge] = []

        for line in lines:
            line = line.split("-")
            
            if line[0] != 'end':
                self.edges.append(Edge(Node(line[0]), Node(line[1])))
            if line[0] != 'start':
                self.edges.append(Edge(Node(line[1]), Node(line[0])))

    def _starting(self, name):
        return list(filter(lambda edge: edge.start.name == name, self.edges))

    def _explorePath(self, currPath: List[Node]):
        startingEdges = self._starting(currPath[-1].name)
        paths = []
        
        for edge in startingEdges:
            currPath.extend([edge.end])
            if edge.end.name == 'end':
                return currPath
            
            currPath.extend(self._explorePath(currPath))

        return currPath

    def explore(self):
        startingEdges = self._starting('start')
        paths = []

        for edge in startingEdges:
            path = [edge.start]
            nextSteps = self._starting(edge.end.name)

            for step in nextSteps:
                newPath = path
                newPath.append(step.start.name)
                newPath.append(step.end.name)
                paths.append(self._explorePath(newPath))


def pp(l: List[Edge]):
    ret = ""

    for edge in l:
        ret += f"{str(edge)}  "

    return ret

