# https://www.codewars.com/kata/582c81d982a0a65424000201
def arr_check(arr):
    return all(isinstance(i, list) for i in arr)


print(arr_check(["A", "R", "R", "A", "Y"]))
