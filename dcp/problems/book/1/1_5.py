"""Given a word w and a string s, find all indices in s which are the starting
locations of anagrams of w.
"""

from collections import defaultdict


def brute(w, s):
    # time: O(sw); space: O(s)
    w_set = set(w)
    n = len(s)
    result = []

    for i in range(n - len(w_set) + 1):
        if w_set == set(s[i : i + len(w)]):
            result.append(i)

    return result


def delete_if_zero(d, char):
    if d[char] == 0:
        del d[char]


def optimal(w, s):
    # time: O(s); space: O(s)
    result = []

    freq = defaultdict(int)
    for char in w:
        freq[char] += 1

    for char in s[: len(w)]:
        freq[char] -= 1
        delete_if_zero(freq, char)

    if not freq:
        result.append(0)

    for i in range(len(w), len(s)):
        start_char, end_char = s[i - len(w)], s[i]
        print(i, start_char, end_char, freq)
        freq[start_char] += 1
        delete_if_zero(freq, start_char)
        print(freq)

        freq[end_char] -= 1
        delete_if_zero(freq, end_char)

        if not freq:
            print(i, start_char, end_char, freq)
            beginning_index = i - len(w) + 1
            result.append(beginning_index)

    return result


assert brute("ab", "abxaba") == [0, 3, 4]
# assert optimal("ab", "abxaba") == [0, 3, 4]
assert optimal("bcd", "b6cbddcb") == [2, 5]
