#  https://leetcode.com/problems/majority-element/
def majorityElement(nums: list[int]) -> int:
    return max(nums, key=nums.count)


nums = [3, 2, 3]
print(majorityElement(nums))
