"""This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not
allowed.
"""

from collections import namedtuple

from dcp import harness


def decode(msg):
    """let m be the message and let i be an index over the message characters.
    Then, the number of ways to decode msg[0, i] equals the number of solutions
    for msg[0, i - 1]) and the number of solutions for msg[0, i - 2] in the
    case that msg[i-2: i] is a valid code.

    consider 1251:
        1 - a
        12 - ab l
        125 - abe le ay
        1251 - abea lea aya

    consider 111:
        1 - a
        11 - aa k
        111 - aaa ka ak
    """
    if not msg:
        return 0

    counts = [0] * len(msg)
    counts[0] = 1

    for i in range(1, len(msg)):
        if int(msg[i - 1 : i + 1]) <= 26:
            # or 1 to handle the case when first two digits are valid
            counts[i] += counts[i - 2] or 1
        counts[i] += counts[i - 1]

    return counts[-1]


if __name__ == "__main__":
    tc = namedtuple("TestCase", "message expected")
    cases = (
        tc("111", 3),
        tc("27", 1),
        tc("26", 2),
        tc("1251", 3),
        tc("81", 1),
        tc("1111", 5),
        tc("1311", 4),
    )

    harness(cases, lambda t: decode(t.message))
