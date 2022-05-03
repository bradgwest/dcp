"""
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer
line length k, return a list of strings which represents each line, fully
justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word. Pad extra spaces when
necessary so that each line has exactly length k. Spaces should be distributed
as equally as possible, with the extra spaces, if any, distributed starting
from the left.

If you can only fit one word on a line, then you should pad the right-hand
side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox",
"jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the
following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""


def pad(line, k):
    current_len = sum(len(word) for word in line) + len(line) - 1
    extra_spaces = k - current_len
    additional = extra_spaces // (len(line) - 1)
    front = extra_spaces % (len(line) - 1)
    out = []
    for i, word in enumerate(line[:-1]):
        word += additional * "•"
        if i < front:
            word += "•"
        out.append(word)
    out.append(line[-1])
    return "•".join(out)


def justify(seq, k):
    """ """
    lines = []
    line = []
    line_chars = 0
    for word in seq:
        if line_chars + 1 + len(word) <= 16:
            line.append(word)
            line_chars += 1 + len(word)
        else:
            lines.append(pad(line, k))
            line = []
            line.append(word)
            line_chars = len(word) + 1

    lines.append(pad(line, k))

    return lines


seq = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
p = justify(seq, 16)
for line in p:
    print(line)
