
nums = [3,0,1]
r = range(len(nums)+1)
sol = list(r)
print (list(set(nums) ^ set(sol))[0])


