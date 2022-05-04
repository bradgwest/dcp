"""This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of
each node holding `next` and `prev` fields, it holds a field named `both`,
which is an XOR of the next node and the previous node. Implement an XOR
linked list; it has an `add(element)` which adds the element to the end, and a
`get(index)` which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you
have access to `get_pointer` and `dereference_pointer` functions that converts
between nodes and memory addresses.
"""

import ctypes


class Node(object):
    def __init__(self, val):
        self.val = val
        self.both = 0


class XorLinkedList(object):
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = []  # This is to prevent garbage collection

    def add(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node

        # Without this line, Python thinks there is no way to reach nodes between
        # head and tail.
        self.__nodes.append(node)

    def get(self, index):
        for i, node in enumerate(l.walk()):
            if i == index:
                return node

        raise IndexError("Linked list index out of range")

    def walk(self):
        prev_id = 0
        node = self.head
        while node is not None:
            next_id = prev_id ^ node.both
            yield node

            if not next_id:
                return

            prev_id = id(node)
            node = _get_obj(next_id)

    def __repr__(self) -> str:
        return " --> ".join([str(n.val) for n in self.walk()])


def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).value


if __name__ == "__main__":
    l = XorLinkedList()
    l.add(Node(1))
    l.add(Node(2))
    l.add(Node(27))
    l.add(Node(3))
    print(l)
