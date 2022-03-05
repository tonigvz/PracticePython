#  https://leetcode.com/problems/smallest-range-ii/
def smallestRangeII(nums: list[int], k: int) -> int:
    res = []
    for i in range(len(nums)):
        if i < (len(nums) - 1):
            res.append(nums[i] + k)
        else:
            res.append(nums[i] - k)
    print(res)
    return max(res) - min(res)


nums = [0, 10]
k = 2
print(smallestRangeII(nums, k))
