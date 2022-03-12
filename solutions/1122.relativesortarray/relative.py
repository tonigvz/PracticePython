#  https://leetcode.com/problems/relative-sort-array/
def relativeSortArray(arr1, arr2):
    res = []
    r = []
    for j in arr2:
        for i in arr1:
            if i == j:
                res.append(j)
    for i in arr1:
        if i not in res:
            r.append(i)
    for i in sorted(r):
        res.append(i)
    return res


nums1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
nums2 = [2, 1, 4, 3, 9, 6]
print(relativeSortArray(nums1, nums2))
