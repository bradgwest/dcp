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


def f(ll):
    # time: O(n); space: O(1)
    prev = ll
    cur = prev.next

    while cur:
        if prev.data > cur.data:
            # swap
            prev.data, cur.data = cur.data, prev.data

        if not cur.next:
            break

        # swap the next
        if cur.next.data > cur.data:
            cur.next.data, cur.data = cur.data, cur.next.data

        prev = cur.next
        cur = cur.next.next

    return ll


ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
expected = Node(1, Node(3, Node(2, Node(5, Node(4)))))
actual = f(ll)
assert str(actual) == str(expected)
