# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
def open_or_senior(data):
    res = []
    for i, j in enumerate(data):
        if j[0] >= 55 and j[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")
    return res


open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)])
