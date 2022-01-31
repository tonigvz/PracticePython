# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
def accum(s):
    res = ''
    for i, c in enumerate(s):
        for j in range(i+1):
            if j == 0:
                res += c.upper()
            else:
                res += c.lower()
        res += "-"
    return res[:-1]


print(accum("NyffsGeyylB"))
