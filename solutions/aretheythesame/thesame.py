# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python
def comp(array1, array2):
    if array1 != None and array2 != None:
        return sorted([i * i for i in array1]) == sorted(array2)
    else:
        return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(a1, a2))
