"""You are given a string of length n and an integer k. The string can be
manipulated by taking one of the first k letters and moving it to the end of
the string.

Write a program to determine the lexicographically smallest string that can
be created after an unlimited number of moves.
"""


def brute(s, k):
    # time: O(k log k); space: O(k)
    results = [s]
    for i in range(k + 1):
        results.append(s[:i] + s[i + 1 :] + s[i])
    return sorted(results)[0]


def optimal(s, k):
    # time: O(n); space: O(1)
    for i in range(1, k + 1):
        if s[i] < s[i - 1]:
            return s[: i - 1] + s[i:] + s[i - 1]

    # None of the first were out of order. We should move the kth character
    # if it's out of order.
    for i in range(k + 1, len(s)):
        if s[k] > s[i]:
            return s[:k] + s[k + 1 :] + s[k]

    return s


assert brute("daily", 1) == "ailyd"
assert brute("daily", 2) == "ailyd"
assert brute("apple", 1) == "aplep"
assert brute("abcd", 1) == "abcd"

assert optimal("daily", 1) == "ailyd"
assert optimal("daily", 2) == "ailyd"
assert optimal("apple", 1) == "aplep"
assert optimal("abcd", 1) == "abcd"
