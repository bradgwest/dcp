class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        d = []
        node = self
        while node is not None:
            d.append(str(node.val))
            node = node.next
        return " -> ".join(d)


class LinkedList:
    def __init__(self) -> None:
        self.head = Node(None, "head")
        self.tail = Node(None, "tail")

    def add(self, node):
        prev = self.get_tail()
        prev.next = node
        node.next = self.tail
        node.prev = prev
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.next = nxt
        nxt.prev = prev

    def get_head(self):
        return self.head.next

    def get_tail(self):
        return self.tail.prev


class LRUCache:
    def __init__(self, n) -> None:
        self.ll = LinkedList()
        self.n = n
        self.cache = {}

    def set(self, k, v):
        if k in self.cache:
            self.cache[k].delete()

        node = Node(k, v)
        self.ll.add(node)
        self.cache[k] = node

        if len(self.cache) > self.n:
            head = self.ll.get_head()
            self.ll.remove(head)
            del self.cache[head.key]

    def get(self, k):
        if k in self.cache:
            node = self.cache[k]
            self.ll.remove(node)
            self.ll.add(node)
            return node.val
