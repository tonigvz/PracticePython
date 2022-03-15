#  https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4/python


def least_larger(a, n):
    res = []
    if a[n] == max(a):
        return -1
    for i in range(len(a)):
        if a[i] > a[n]:
            res.append(a[i])
    return a.index(min(res))


print(least_larger([1, 3, 5, 2, 4], 0))
