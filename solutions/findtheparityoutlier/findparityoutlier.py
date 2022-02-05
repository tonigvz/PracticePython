# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
def find_outlier(integers):
    res = []
    res2 = []
    for i in integers:
        if i % 2 == 0:
            res.append(i)
        else:
            res2.append(i)

    return res[-1] if len(res) == 1 else res2[-1]


print(find_outlier([2, 4, 6, 8, 10, 3]))
