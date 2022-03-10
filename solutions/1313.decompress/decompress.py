#  https://leetcode.com/problems/decompress-run-length-encoded-list/
def decompressRLElist(nums):
    res2 = []
    for i in range(0, len(nums), 2):
        fv = nums[0 + i : 2 + i]
        list = [fv[1] for i in range(fv[0])]
        res2 += list
    return res2


nums = [1, 2, 3, 4]
print(decompressRLElist(nums))
