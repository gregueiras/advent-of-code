import sys
import math

debug = True or len(sys.argv) >= 2


class Node:
    id = 0

    def __init__(self, value='', parent=None) -> None:
        self.value = value
        self.parent = parent
        self.left = self.right = None
        self.id = Node.id

        Node.id += 1

    def hasChildren(self) -> bool:
        return self.left is not None or self.right is not None

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"

        if self.left is not None:
            ret += self.left.__str__(level+1)
        if self.right is not None:
            ret += self.right.__str__(level+1)

        return ret

    def __repr__(self) -> str:
        return str(self.value)


def buildNode(n, parent=None):
    if not isinstance(n, list):
        return Node(n, parent)

    node = Node('')
    node.left = buildNode(n[0], node)
    node.right = buildNode(n[1], node)

    return node


def printTree(node, level=0):
    if node != None:
        if node.left is not None:
            node.left.parent = node
        printTree(node.left, level + 1)
        if debug:
            print('-' * 4 * level + str(node.id) + '->', node.value)
        else:
            print('-' * 4 * level + '->', node.value)

        if node.right is not None:
            node.right.parent = node
        printTree(node.right, level + 1)


def initTree(node):
    if node != None:
        if node.left is not None:
            node.left.parent = node
        initTree(node.left)

        if node.right is not None:
            node.right.parent = node
        initTree(node.right)


def bubbleLeft(node, val):
    if node is None:
        return

    if node.left is not None and node.left.value != '':
        node.left.value += val
        return

    bubbleLeft(node.parent, val)


def bubbleRight(node, val):
    if node is None:
        return

    if node.right is not None and node.right.value != '':
        node.right.value += val
        return

    if node.right is not None and node.parent is None:
        sinkLeft(node.right, val)

    bubbleRight(node.parent, val)


def sinkLeft(node, val):
    if node is None:
        return

    if node.left is not None:
        if node.left.value == '':
            sinkLeft(node.left, val)
        else:
            node.left.value += val
            return

    if node.right is not None:
        if node.right.value == '':
            sinkLeft(node.left, val)
        else:
            node.right.value += val
            return


actionFound = False


def explode(node, level=0):
    global actionFound

    if actionFound == True:
        return
    if node != None:
        if level > 3:
            toExit = False
            if node.left is not None:
                val = node.left.value
                node.left = None

                node.value = ''
                bubbleLeft(node.parent, val)
                node.value = 0
                toExit = True

            if node.right is not None:
                val = node.right.value
                node.right = None

                node.value = ''
                bubbleRight(node.parent, val)
                node.value = 0
                toExit = True

            if toExit:
                print(f"EXPLODE {val} - {node.id}")
                actionFound = True
                return True

        if node.left is None and node.right is None and isinstance(node.value, int) and node.value >= 10:
            val = node.value

            node.left = Node(math.floor(val / 2), node)
            node.right = Node(math.ceil(val / 2), node)
            node.value = ''

            print(f"SPLIT {val}")
            actionFound = True
            return True

        ret = explode(node.left, level + 1)
        if ret or actionFound:
            return
        ret = explode(node.right, level + 1)
        if ret or actionFound:
            return


def add(nodeA: Node, nodeB: Node) -> Node:
    node = Node()
    node.left = nodeA
    node.right = nodeB

    nodeA.parent = node
    nodeB.parent = node

    return node


def printLine(node):
    ret = ""
    if node is None:
        return

    if node.value != '':
        return str(node.value)

    ret += "["
    ret += printLine(node.left)
    ret += ","
    ret += printLine(node.right)
    ret += "]"

    return ret


""" homework = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    #[5, 5],
] """

homework = [
    [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
    [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
]

nodeA = buildNode(homework[0])
initTree(nodeA)
nodeB = buildNode(homework[1])
initTree(nodeB)

acc = add(nodeA, nodeB)
prevAcc = None

while prevAcc != printLine(acc):
    prevAcc = printLine(acc)
    explode(acc)
    actionFound = False


for i in range(2, len(homework)):
    newNode = buildNode(homework[i])
    initTree(newNode)
    acc = add(acc, newNode)

    prevAcc = None
    while prevAcc != printLine(acc):
        prevAcc = printLine(acc)
        explode(acc)
        actionFound = False


res = printLine(acc)
expected = [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]

print(res)
print(res == str(expected))
