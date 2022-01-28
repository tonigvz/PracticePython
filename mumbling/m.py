# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
def accum(s):
    res = []
    for i in s:
        q = s.index(i)
        sum = i * q
        res.extend([i.capitalize(), sum])
    rex = "".join(res)
    print(rex)


accum("abcd")
