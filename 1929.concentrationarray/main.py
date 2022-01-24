nums = [1, 3, 2, 1]
num = []
r = 2 * len(nums)
print(r)

while len(num) < r:
    for i in nums:
        num.append(i)

print(num)
