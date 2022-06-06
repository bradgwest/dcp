class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

    def __str__(self) -> str:
        d = []
        node = self
        while node is not None:
            d.append(str(node.data))
            node = node.next
        return " -> ".join(d)


def intersect(a, b):
    # time: O(m + n); space: O(1)
    n = m = 0
    node = a
    while node is not None:
        n += 1
        node = node.next

    node = b
    while node is not None:
        m += 1
        node = node.next

    if n - m > 0:
        left, right = a, b
        skip = n - m
    else:
        left, right = b, a
        skip = m - n

    for _ in range(skip):
        left = left.next

    # at this point, left and right, they have the same length
    while not (left is None or right is None):
        if left is right:
            return left
        left, right = left.next, right.next


common = Node(8, Node(10))
a = Node(3, Node(7, common))
b = Node(99, Node(1, common))
assert intersect(a, b) == common

a = Node(3, Node(4))
b = Node(5, Node(3))
assert intersect(a, b) is None
