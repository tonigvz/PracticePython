#https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/solutions/python
def solution(nums):
    if nums == None:
        return []
    else:
        res = list(nums)
        res.sort()
        return res

nums = [1,2,3,10,5]
print(solution(nums))