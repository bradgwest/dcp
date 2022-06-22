import operator


class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


op = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def evaluate(node):
    if node.data not in op:
        return node.data

    if node.data in op:
        return op[node.data](evaluate(node.left), evaluate(node.right))


tree = Node("*", Node("+", Node(3), Node(2)), Node("+", Node(4), Node(5)))
actual = evaluate(tree)
assert actual == 45

tree = Node("/", Node(12), Node(3))
assert evaluate(tree) == 4

tree = Node("+", Node(1), Node("*", Node(3), Node(6)))
assert evaluate(tree) == 19
