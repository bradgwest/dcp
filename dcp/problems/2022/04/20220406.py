"""Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k
distinct characters is "bcb".
"""

from collections import namedtuple

from dcp import harness


def substr(s, k):
    if k < 1 or not s:
        return 0

    max_len = 0
    # keys are the characters in the current substring
    # value is index of the character's last occurrence in the substring
    chars = {}
    # start and end of the current substring
    bounds = 0, 0
    for i, char in enumerate(s):
        chars[char] = i
        if len(chars) <= k:
            new_lowest_bound = bounds[0]
        else:
            new_lowest_bound = chars.pop(min(chars, key=chars.get)) + 1

        bounds = new_lowest_bound, bounds[1] + 1
        max_len = max(max_len, bounds[1] - bounds[0])

    return max_len


if __name__ == "__main__":
    tc = namedtuple("TestCase", "s k expected")
    cases = (
        tc("abcba", 2, 3),
        tc("aabc", 1, 2),
        tc("ceabfddbaa", 3, 5),
        tc("", 3, 0),
    )

    harness(cases, lambda t: substr(t.s, t.k))
