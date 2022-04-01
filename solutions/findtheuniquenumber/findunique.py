#  https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
from collections import Counter


def find_uniq(arr):
    c = Counter(arr)
    return min(c, key=c.get)


print(find_uniq([1, 1, 1, 2, 1, 1]))
