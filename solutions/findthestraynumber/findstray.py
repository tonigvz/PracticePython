# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
from collections import Counter


def stray(arr):
    dict = Counter(arr)
    return [key for key, value in dict.items() if value == 1][-1]


print(stray([17, 17, 3, 17, 17, 17, 17]))
