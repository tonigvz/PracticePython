#  https://leetcode.com/problems/intersection-of-two-arrays/
def intersection(nums1, nums2):
    arr1 = set(nums1)
    arr2 = set(nums2)
    return arr1.intersection(arr2)


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))
