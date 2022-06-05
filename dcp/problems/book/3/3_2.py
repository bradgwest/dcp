"""Given two linked lists in reversed number format (532 -> 2 - 3 - 5), return
their sum.
"""


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


def add(a, b):
    head = Node(0)
    current = head
    while not (a is None and b is None):
        x = a.data if a is not None else 0
        y = b.data if b is not None else 0

        carry, remainder = (x + y) // 10, (x + y) % 10
        current.data += remainder
        current.next = Node(carry)
        current = current.next

        a = a.next
        b = b.next

    return head


a1 = Node(9, Node(9))
b1 = Node(5, Node(2))
c1 = Node(4, Node(2, Node(1)))
# print(add(a1, b1))
assert str(add(a1, b1)) == str(c1)
