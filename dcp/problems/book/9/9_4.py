import heapq


class Node:
    def __init__(self, char, left=None, right=None) -> None:
        self.char = char
        self.left = left
        self.right = right

    def __repr__(self):
        fmt = "{}({char!r}"
        if self.left is not None:
            fmt += ", {left!r}"
        else:
            fmt += ","
        if self.right is not None:
            fmt += ", {right!r})"
        else:
            fmt += ",)"
        return fmt.format(type(self).__name__, **vars(self))


def build_tree(freqs):
    nodes = []
    for char, freq in freqs.items():
        heapq.heappush(nodes, (freq, Node(char)))

    while len(nodes) > 1:
        # pull the two least used characters off the priority queue
        f1, c1 = heapq.heappop(nodes)
        f2, c2 = heapq.heappop(nodes)
        parent = Node("*", left=c1, right=c2)
        heapq.heappush(nodes, (f1 + f2, parent))

    # the root node
    return nodes[0][1]


def encode(node, string="", code={}):
    if not node:
        return

    if not (node.left or node.right):
        code[node.char] = string
        return

    encode(node.left, string + "0", code)
    encode(node.right, string + "1", code)

    return code


frequencies = {"a": 3, "c": 6, "e": 8, "f": 2}
root = build_tree(frequencies)
print(encode(root))
