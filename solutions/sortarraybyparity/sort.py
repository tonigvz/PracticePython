def sortArrayByParity(nums):
    res = []
    res2 = []
    for i in nums:
        if i % 2 == 0:
            res.append(i)
        else:
            res2.append(i)
    return res + res2


nums = [3, 1, 2, 4]
print(sortArrayByParity(nums))
