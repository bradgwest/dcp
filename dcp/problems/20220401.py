"""This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the node to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

from collections import namedtuple

from dcp import harness


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def count_univals_slow(node):
    """
    runtime: O(n^2) because for every node in the tree we count all its
      subtrees
    space: O(n) for the tree
    """
    if node.left is None and node.right is None:
        return 1

    left = count_univals(node.left)
    right = count_univals(node.right)

    additional = 0
    if (
        right
        and (node.right is None or node.right.value == node.value)
        and left
        and (node.left is None or node.left.value == node.value)
    ):
        additional = 1
    return left + right + additional


def count_univals(node):
    """
    runtime: O(n) because we iterate once over every node in the tree
    space: O(n) for the tree
    """

    def _helper(node):
        # A None node is itself a unival tree but has 0 sub unival trees
        if node is None:
            return 0, True

        left_count, is_left_unival = _helper(node.left)
        right_count, is_right_unival = _helper(node.right)
        total_count = left_count + right_count

        if is_left_unival and is_right_unival:
            if node.left is not None and node.value != node.left.value:
                return total_count, False
            if node.right is not None and node.value != node.right.value:
                return total_count, False
            return total_count + 1, True
        return total_count, False

    return _helper(node)[0]


if __name__ == "__main__":
    tc = namedtuple("TestCase", "tree expected")
    cases = (
        tc(Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))), 5),
        tc(Node(0), 1),
        tc(Node(1, Node(1), Node(1)), 3),
    )
    harness(cases, lambda t: count_univals(t.tree))
