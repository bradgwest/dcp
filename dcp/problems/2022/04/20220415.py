"""This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible
reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond]
or ['bedbath', 'and', 'beyond'].
"""


def greedy(shortened, words):
    sentence = []
    word = ""
    for char in shortened:
        word += char
        if word in words:
            sentence.append(word)
            word = ""

    return sentence


def find_sentence(s, dictionary):
    starts = {0: ""}
    for i in range(len(s) + 1):
        new_starts = {}
        for start_index, _ in starts.items():
            word = s[start_index:i]
            if word in dictionary:
                new_starts[i] = word
        starts.update(new_starts)

    result = []
    current_length = len(s)
    if current_length not in starts:
        return None

    while current_length:
        word = starts[current_length]
        result.append(word)
        current_length = current_length - len(word)

    return list(reversed(result))


shortened = "theremin"
words = {"the", "theremin"}
print(find_sentence(shortened, words))

shortened = "thequickbrownfox"
words = {"quick", "brown", "the", "fox"}
print(find_sentence(shortened, words))

shortened = "bedbathandbeyond"
words = {"bed", "bath", "bedbath", "and", "beyond"}
print(find_sentence(shortened, words))
