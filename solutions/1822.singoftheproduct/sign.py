#  https://leetcode.com/problems/sign-of-the-product-of-an-array/
import math


def arraySign(nums: list[int]) -> int:
    product = math.prod(nums)
    if product > 0:
        return 1
    elif product == 0:
        return 0
    else:
        return -1


nums = [1, 5, 2, 2, -3]
print(arraySign(nums))
