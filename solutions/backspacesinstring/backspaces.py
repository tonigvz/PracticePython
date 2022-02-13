# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python
from re import I


def clean_string(s):
    res = ""
    for i, j in enumerate(s):
        if j == "#":
            res = res[:-1]
        else:
            res += j
    return res


clean_string("abc#d##c")
