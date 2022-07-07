class Trie:
    ENDS_HERE = "#"

    def __init__(self) -> None:
        self._trie = {}

    def insert(self, word):
        trie = self._trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[self.ENDS_HERE] = True

    def find(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return None
        return trie


def leaves(trie, result, suffixes=None):
    if suffixes is None:
        suffixes = []

    for k, v in trie.items():
        if k == Trie.ENDS_HERE:
            result.append("".join(suffixes))
        else:
            leaves(v, result, [*suffixes, k])


def autocomplete(trie, prefix):
    trie = trie.find(prefix)
    if trie is None:
        return None

    result = []
    leaves(trie, result, [prefix])
    return result


words = ["dog", "bear", "cat", "coat"]
trie = Trie()
for word in words:
    trie.insert(word)

print(autocomplete(trie, "be"))
