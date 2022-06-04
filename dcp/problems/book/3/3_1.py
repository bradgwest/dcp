"""Given the head of a singly linked list, reverse it in place.
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


def reverse(node):
    # time: O(n) space: O(n)
    head, _ = _reverse(node)
    return head


def _reverse(node):
    # empty node
    if node is None:
        return None, None

    # single node
    if node.next is None:
        return node, node

    # more than one node
    head, tail = _reverse(node.next)

    # set existing node to last
    node.next = None
    tail.next = node

    return head, node


def optimal(node):
    # time: O(n); space O(1)
    if node is None:
        return None

    prev, current = None, node
    while current is not None:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp

    return prev


zero = None
single = Node(1)
double = Node(1, Node(2))
triple = Node(1, Node(2, Node(3)))

# print(reverse(zero))
# print(reverse(single))
# print(reverse(double))
# print(reverse(triple))

print(optimal(zero))
print(optimal(single))
print(optimal(double))
print(optimal(triple))
