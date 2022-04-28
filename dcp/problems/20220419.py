"""This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from
the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""


class Node:
    def __init__(self, val, nxt=None) -> None:
        self.val = val
        self.next = nxt


def remove(node, k):
    """ """
    result = node

    # advance to the kth node
    for _ in range(k):
        node = node.next

    while node and node.next is not None:
        node = node.next
        result = result.next

    return result


l = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(remove(l, 2).val)

l = Node(1)
print(remove(l, 1).val)

l = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(remove(l, 3).val)
