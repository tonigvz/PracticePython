#  https://www.codewars.com/kata/598f76a44f613e0e0b000026/train/python
import re


def sum_of_integers_in_string(s):
    return sum(int(i) for i in re.findall("\d+", s))


print(sum_of_integers_in_string("12.4"))
