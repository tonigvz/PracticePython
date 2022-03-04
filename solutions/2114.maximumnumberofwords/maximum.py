#  https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
def mostWordsFound(sentences: list[str]) -> int:
    return max([len(i.split()) for i in sentences])


sentences = [
    "alice and bob love leetcode",
    "i think so too",
    "this is great thanks very much",
]
print(mostWordsFound(sentences))
