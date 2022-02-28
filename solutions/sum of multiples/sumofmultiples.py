#  https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python
def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    else:
        res = 0
        for i in range(0, m, n):
            res += i
    return res
