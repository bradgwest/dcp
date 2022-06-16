class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


def is_unival(node, val=None):
    if val is None:
        val = node.data
    elif node is None:
        return True
    elif node.data != val:
        return False

    return is_unival(node.left, val) and is_unival(node.right, val)


def count_unival(node):
    if node is None:
        return 0
    return int(is_unival(node)) + count_unival(node.left) + count_unival(node.right)


tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
assert count_unival(tree) == 5
