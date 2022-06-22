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


def reconstruct(in_order, pre_order):
    if not pre_order and not in_order:
        return None

    root_value = pre_order[0]
    root = Node(root_value)

    if len(pre_order) == len(in_order) == 1:
        return root

    root_idx = in_order.index(root_value)
    root.left = reconstruct(in_order[:root_idx], pre_order[1 : 1 + root_idx])
    root.right = reconstruct(in_order[root_idx + 1 :], pre_order[1 + root_idx :])
    return root


pre_order = list("abdecfg")
in_order = list("dbeafcg")
expected = Node("a", Node("b", Node("d"), Node("e")), Node("c", Node("f"), Node("g")))
actual = reconstruct(in_order, pre_order)
print(actual)
assert str(actual) == str(expected)
