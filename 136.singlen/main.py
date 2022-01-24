def solution():
    nums = [0, 0, 1, 2]
    sol = []
    for i in nums:
        if nums.count(i) == 1:
            sol.append(nums[i])
    print(sol)


solution()
