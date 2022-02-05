# https://www.codewars.com/kata/57eb936de1051801d500008a/train/python
def explode(arr):
    if any(value.isnumeric() for value in str(arr)):
        sums = sum(i for i in arr if type(i) is int)
        return [arr for j in range(sums)]
    else:
        return "Void!"


print(explode(['a', 3]))
