"""Given a list of words, find all pairs of unique indexes such that the
concatenation of the two words is a palindrome.
"""


def is_palindrome(word):
    return word == word[::-1]


def brute(words):
    # time: O(n); space: O(n)
    n = len(words)
    result = []

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if is_palindrome(words[i] + words[j]):
                result.append((i, j))

    return result


def optimal(words):
    # time: O(n*c^2); space: O(n)
    cache = {}
    for i, word in enumerate(words):
        cache[word] = i

    result = []

    for i, word in enumerate(words):
        for char_i in range(len(word)):
            prefix, suffix = word[:char_i], word[char_i:]
            reversed_prefix, reversed_suffix = prefix[::-1], suffix[::-1]

            p = cache.get(reversed_prefix)
            if is_palindrome(suffix) and p not in (i, None):
                result.append((i, p))

            s = cache.get(reversed_suffix)
            if is_palindrome(prefix) and s not in (i, None):
                result.append((i, s))

    return result


assert brute(["code", "edoc", "da", "d"]) == [(0, 1), (1, 0), (2, 3)]
assert optimal(["code", "edoc", "da", "d"]) == [(0, 1), (1, 0), (2, 3)]
