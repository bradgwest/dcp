"""Implement an autocomplete system. That is, given a query string s and a
set of all possible query strings, return all strings in the set that have
s as a prefix.

For example, given the query string de and the set of strings [dog, deer,
deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to
speed up queries.
"""

from collections import namedtuple

from dcp import harness

WORD_END = "__WORK_END"


class Trie:
    def __init__(self) -> None:
        self._trie = {}

    def insert(self, word):
        trie = self._trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[WORD_END] = True

    def elements(self, prefix):
        d = self._trie
        for char in prefix:
            if char in d:
                d = d[char]
            else:
                return []
        return self._elements(d)

    def _elements(self, d):
        result = []
        for c, v in d.items():
            if c == WORD_END:
                subresult = [""]
            else:
                subresult = [c + suffix for suffix in self._elements(v)]
            result.extend(subresult)
        return result


def autocomplete(s, trie):
    """
    runtime: O(n) worst case
    """
    return [s + suffix for suffix in trie.elements(s)]


if __name__ == "__main__":
    tc = namedtuple("TestCase", "s expected")
    words = [
        "dog",
        "deer",
        "deal",
        "dig",
        "tin",
        "cup",
        "mountains",
        "mammoth",
        "millions",
    ]

    trie = Trie()
    for word in words:
        trie.insert(word)

    cases = (
        tc("de", ["deer", "deal"]),
        tc("pop", []),
        tc("m", ["mountains", "mammoth", "millions"]),
        tc("mam", ["mammoth"]),
    )

    harness(cases, lambda t: autocomplete(t.s, trie))
