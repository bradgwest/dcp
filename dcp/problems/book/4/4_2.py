def is_matching(opening, closing):
    return (
        (opening == "(" and closing == ")")
        or (opening == "{" and closing == "}")
        or (opening == "[" and closing == "]")
    )


def balanced(s):
    opening = "({["
    closing = ")}]"
    stack = []

    for bracket in s:
        if bracket in opening:
            stack.append(bracket)
        elif bracket in closing:
            if not is_matching(stack.pop(), bracket):
                return False
        else:
            raise ValueError("invalid input string")

    if stack:
        return False

    return True


assert balanced("{[]}()[{()}]") is True
assert balanced("{[)}") is False
assert balanced("{[]") is False
