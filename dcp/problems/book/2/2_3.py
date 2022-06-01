"""Given a string and a number of lines k, print the string in zigzag form
"""


def construct(line):
    l = [("", 0)] + line
    spaces = [(" ", y[1] - x[1]) for x, y in zip(l[:], l[1:])]
    print(spaces)
    out = []
    for char, _ in line:
        space, num = spaces.pop(0)
        for _ in range(num):
            out.append(space)
        out.append(char)
    return "".join(out)


def zigzag(s, k):
    # time: O(n); space: O(n)
    coords = [[] for _ in range(k)]

    x, y = 0, 0
    down = True
    for char in s:
        coords[y].append((char, x))
        # update coordinates
        x += 1
        # reverse direction
        if y == k - 1:
            down = False
        elif y == 0:
            down = True

        if down:
            y += 1
        else:
            y -= 1

    print(coords)
    for line in coords:
        print(construct(line))


zigzag("thisisazigzag", 4)
