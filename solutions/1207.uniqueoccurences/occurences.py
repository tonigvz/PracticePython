#  https://leetcode.com/problems/unique-number-of-occurrences/
from collections import Counter


def uniqueOccurences(arr):
    count = Counter(arr)
    res = [count[i] for i in count]
    return len(set(res)) == len(res)


arr = [1, 2, 2, 1, 1, 3]
print(uniqueOccurences(arr))
