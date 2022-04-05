#  https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python
def parse(data):
    res = []
    r = 0
    for i in data:
        if i == "i":
            r += 1
        elif i == "d":
            r -= 1
        elif i == "s":
            r = r ** 2
        elif i == "o":
            res.append(r)
    return res


print(parse("iiisdoso"))
