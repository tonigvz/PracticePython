class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        k = []

        for i in range(len(nums)):
            s = target - nums[i]
            if s in nums:
                if i is not nums.index(s):
                    k.append(i)
                    k.append(nums.index(s))
                    return k
