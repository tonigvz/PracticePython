#  https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
def dig_pow(n, p):
    res = 0
    for i in str(n):
        res += int(i) ** p
        p += 1
    k = int(res / n)
    if res == n * k:
        return k
    return -1


print(dig_pow(46288, 3))
