"""This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
"""


def encode(word):
    out = []
    current = None
    count = 0
    for char in word:
        if current is None or char == current:
            count += 1
        else:
            out.extend([str(count), current])
            count = 1
        current = char
    out.extend([str(count), current])
    return "".join(out)


def decode(word):
    out = []
    for i in range(0, len(word), 2):
        n, char = word[i : i + 2]
        out.extend([char] * int(n))
    return "".join(out)


word = "AAAABBBCCDAA"
assert decode(encode(word)) == word
