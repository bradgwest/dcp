"""Given two singly linked lists that intersect at some point, find the
intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return
the node with value 8.

In this example, assume nodes with the same value are the exact same node
objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and
constant space.
"""


class Node:
    def __init__(self, val, nxt=None) -> None:
        self.val = val
        self.next = nxt


a = Node(3)
node = a
for i in [7, 8, 10]:
    new_node = Node(i)
    node.next = new_node
    node = new_node

b = Node(99)
b.next = Node(1)
b.next.next = a.next.next

assert a.next.next.val == 8
assert a.next.next is b.next.next


def find_common(a, b):
    a_len, b_len = 0, 0
    node = a
    while node:
        a_len += 1
        node = node.next

    node = b
    while node:
        b_len += 1
        node = node.next

    diff = b_len - a_len
    if diff < 0:
        diff *= -1
        first = a
        second = b
    else:
        first = b
        second = a

    for _ in range(diff):
        first = first.next

    # at this point the lists have the same length
    while first is not second:
        first = first.next
        second = second.next

    return first


# a = 3 -> 7 -> 8 -> 10; b = 99 -> 1 -> 8 -> 10
common = Node(8, Node(10))
a = Node(3, Node(7, common))
b = Node(99, Node(1, common))
assert find_common(a, b) == b.next.next

# a = 4, 5; b = 2, 3, 4, 5
a = Node(4, Node(5))
b = Node(2, Node(3, a))
assert find_common(a, b) == a
