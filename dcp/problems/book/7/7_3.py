class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        fmt = "{}({data!r}"
        if self.left is not None:
            fmt += ", {left!r}"
        else:
            fmt += ","
        if self.right is not None:
            fmt += ", {right!r})"
        else:
            fmt += ",)"
        return fmt.format(type(self).__name__, **vars(self))


def helper(start, stop):
    trees = []

    if start > stop:
        trees.append(None)
        return trees

    for x in range(start, stop + 1):
        left = helper(start, x - 1)
        right = helper(x + 1, stop)

        for l in left:
            for r in right:
                node = Node(x, l, r)
                trees.append(node)

    return trees


def trees(n):
    tree_list = helper(1, n)
    for tree in tree_list:
        print(tree)


trees(3)
