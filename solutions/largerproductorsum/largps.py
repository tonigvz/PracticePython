#  https://www.codewars.com/kata/5c4cb8fc3cf185147a5bdd02/train/python
def sum_or_product(arr, n):
    sum = 0
    prod = 1
    s = sorted(arr)
    l = len(arr)
    for i in s[l - n : l]:
        sum += i
    for i in s[0:n]:
        prod *= i
    return "product" if prod > sum else "same" if prod == sum else "sum"


print(sum_or_product([10, 41, 8, 16, 20, 36, 9, 13, 20], 3))
