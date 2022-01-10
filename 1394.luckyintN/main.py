arr = [5,4,7,8,4,8,8,3,7,7,6,3,7,6,5,6,8,4,5,7,4,7,7,5,2,5,6,6,8,1,6,8,8,8,9,3,2,9]
sol = -1
for i in arr:
    if arr.count(i) == i:
        sol = i
print(max(sol))
#does not work
#actual solution is :  return max(i if arr.count(i) == i else -1 for i in arr)