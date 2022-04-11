#  https://www.codewars.com/kata/58670300f04e7449290000e5/train/python
def longest(words):
    return max([len(i) for i in words])


print(longest(["simple", "is", "better", "than", "complex"]))
