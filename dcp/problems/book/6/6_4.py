import collections


class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


def bfs(node, d):
    if node is None:
        return

    level = 0
    q = [(node, level)]

    while q:
        node, level = q.pop(0)
        d[level] += node.data

        if node.left is not None:
            q.append((node.left, level + 1))

        if node.right is not None:
            q.append((node.right, level + 1))


def ms(node):
    sums = collections.defaultdict(int)
    bfs(node, sums)

    min_level = None
    min_val = float("inf")
    for level, val in sums.items():
        if val < min_val:
            min_level = level
            min_val = val

    return min_level


# tree = Node(1, Node(2), Node(3, Node(4), Node(5)))
# assert ms(tree) == 0


tree = Node(4, Node(2), Node(1, Node(0), Node(1)))
actual = ms(tree)
assert actual == 2
