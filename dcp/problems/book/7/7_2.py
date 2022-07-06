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


def f(arr):
    if not arr:
        return

    n = len(arr)
    if n == 1:
        return Node(arr[0])

    midpoint = len(arr) // 2
    return Node(arr[midpoint], f(arr[:midpoint]), f(arr[midpoint + 1 :]))


arr = [-1, 5, 6, 7, 10, 25]
print(f(arr))
print(f([-1]))
print(f([5, 6]))
print(f([5, 6, 7]))
print(Node(6, Node(5), Node(7)))
