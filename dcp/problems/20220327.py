"""
Good morning!

This is your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string
back into the tree.

For example, given the following Node class

```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
"""

import json


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_dict(self):
        d = {}
        d["val"] = self.val

        if self.left is None:
            d["left"] = None
        else:
            d["left"] = self.left.to_dict()

        if self.right is None:
            d["right"] = None
        else:
            d["right"] = self.right.to_dict()

        return d

    @classmethod
    def from_dict(cls, d):
        if d is None:
            return None
        return cls(d["val"], cls.from_dict(d["left"]), cls.from_dict(d["right"]))

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, s):
        return cls.from_dict(json.loads(s))


def serialize(node):
    return node.to_json()


def deserialize(s):
    return Node.from_json(s)


if __name__ == "__main__":
    node = Node("root", Node("left", Node("left.left")), Node("right"))
    assert deserialize(serialize(node)).left.left.val == "left.left"

    node = Node("root")
    assert deserialize(serialize(node)).val == "root"
