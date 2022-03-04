#  https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    lst = []
    for i in nums:
        count = 0
        for j in nums:
            if i > j:
                count += 1
        lst.append(count)
    return lst


nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums))
