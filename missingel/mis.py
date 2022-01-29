# https://www.codewars.com/kata/5299413901337c637e000004/train/python
def get_missing_element(seq):
    replace = [i for i in range(10)]
    res = "".join([str(i) for i in replace if i not in seq])
    return int(res)


num = [9, 2, 4, 5, 7, 0, 8, 6, 1]
get_missing_element(num)
