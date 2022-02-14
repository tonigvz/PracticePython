# https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python
def data_reverse(data):
    res = []
    res2 = []
    for i in range(0, len(data), 8):
        res.append(data[i : i + 8])
    for i in reversed(res):
        res2.extend(i)
    return res2


data1 = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
]

print(data_reverse(data1))
