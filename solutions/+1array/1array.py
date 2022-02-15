# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python
def up_array(arr):
    if len(arr) < 1:
        return None

    for i in arr:
        if i < 0 or len(str(i)) > 1:
            return None

    return [int(i) for i in str(int("".join(str(i) for i in arr)) + 1)]


up_array([2, 3, 9])
