#  https://leetcode.com/problems/delete-columns-to-make-sorted/
def minDeletionSize(strs: list[str]) -> int:
    count = 0
    res = ["".join(sorted(i)) for i in strs]
    for i in range(len(strs)):
        if strs[i] != res[i]:
            count += 1
    return count


strs = ["cba", "daf", "ghi"]
print(minDeletionSize(strs))
