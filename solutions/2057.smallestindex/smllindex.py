#https://leetcode.com/problems/smallest-index-with-equal-value/
def smallestEqual(nums):
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
    return -1

    




num =  [4,3,2,1]
print(smallestEqual(num))