class PrefixMapSum:
    ENDS_HERE = "#"

    def __init__(self) -> None:
        self._trie = {}

    def insert(self, word, value):
        trie = self._trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[self.ENDS_HERE] = value

    def _find(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return None
        return trie

    def sum(self, prefix):
        trie = self._find(prefix)
        if trie is None:
            return 0

        result = 0

        for k, v in trie.items():
            if k == PrefixMapSum.ENDS_HERE:
                result += v
            else:
                result += self.sum(prefix + k)

        return result


pms = PrefixMapSum()
words = [
    ("dog", 1),
    ("doggie", 2),
    ("doge", 3),
    ("cat", 2.5),
    ("tomcat", 6),
    ("topgun", 100),
]
for word, value in words:
    pms.insert(word, value)

print(pms.sum("a"))
