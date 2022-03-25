#  https://www.codewars.com/kata/53f103c3ef9ad4014f00013b/train/python
def find_most_frequent(l):
    res = set()
    for i in l:
        if l.count(i) == max([l.count(y) for y in l]):
            res.add(i)
    return res


print(find_most_frequent([1, 1, 2, 3]))
