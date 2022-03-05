#   https://leetcode.com/problems/shuffle-the-array/
def shuffle(nums, n):
    res = []
    for i in range(int(len(nums) / 2)):
        res.append(nums[0 + i])
        res.append(nums[n + i])
    return res


nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
print(shuffle(nums, n))
