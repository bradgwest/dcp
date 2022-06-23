class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


def bounds(root, x, floor=None, ceil=None):
    if root is None:
        return floor, ceil

    if root.data == x:
        return x, x

    if x < root.data:
        floor, ceil = bounds(root.left, x, floor, root.data)

    if x > root.data:
        floor, ceil = bounds(root.right, x, root.data, ceil)

    return floor, ceil


tree = Node(7, Node(5, Node(-1), Node(6)), Node(10, None, Node(25)))
actual = bounds(tree, 8)
assert actual == (7, 10)
