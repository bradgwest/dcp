from collections import defaultdict


def fewest_cuts(wall):
    cuts = defaultdict(int)

    for bricks in wall:
        length = 0
        for brick in bricks[:-1]:
            length += brick
            cuts[length] += 1

    return len(wall) - max(cuts.values())


wall = [[3, 5, 1, 1], [2, 3, 3, 2], [5, 5], [4, 4, 2], [1, 3, 3, 3], [1, 1, 6, 1, 1]]
assert fewest_cuts(wall) == 2
