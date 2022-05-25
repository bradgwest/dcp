"""This problem was asked by Google.

The edit distance between two strings refers to the minimum number of
character insertions, deletions, and substitutions required to change one
string to the other. For example, the edit distance between “kitten” and
“sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”,
and append a “g”.

Given two strings, compute the edit distance between them.
"""


def p(arr):
    for row in arr:
        print(row)
    print()


def edit_distance(a, b):
    # initialize array:
    arr = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]

    for i in range(len(a) + 1):
        arr[i][0] = i

    for j in range(len(b) + 1):
        arr[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                insertion = 1 + arr[i][j - 1]
                deletion = 1 + arr[i - 1][j]
                replacement = 1 + arr[i - 1][j - 1]

                arr[i][j] = min(insertion, deletion, replacement)

    return arr[len(a)][len(b)]


a = "kitten"
b = "sitting"
print(edit_distance(b, a))
