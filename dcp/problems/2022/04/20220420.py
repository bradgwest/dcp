"""This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

from collections import deque


def match(left, right):
    return (
        (left == "(" and right == ")")
        or (left == "[" and right == "]")
        or (left == "{" and right == "}")
    )


def balanced(brackets):
    stack = deque()
    for bracket in brackets:
        if bracket in "([{":
            # push opening bracket
            stack.append(bracket)
            continue

        # closing bracket
        if not stack or not match(stack.pop(), bracket):
            return False

    if stack:
        return False

    return True


print(balanced("([])[]({})"))
print(balanced("([)]"))
print(balanced("((()"))
