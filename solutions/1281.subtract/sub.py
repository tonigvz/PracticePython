#  https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
def subtractProductAndSum(n):
    prod = 1
    sum = 0
    for i in str(n):
        prod *= int(i)
    for i in str(n):
        sum += int(i)
    return prod - sum


Number = 4421
print(subtractProductAndSum(Number))
