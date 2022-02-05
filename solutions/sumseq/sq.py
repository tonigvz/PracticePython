# https://www.codewars.com/kata/52774a314c2333f0a7000688/python
from itertools import count


def sequence_sum(begin_number, end_number, step):
    return sum([i for i in range(begin_number, end_number + 1, step)])


print(sequence_sum(1, 5, 3))
