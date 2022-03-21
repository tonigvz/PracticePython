#  https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python
def parts_sums(ls):
    res = [sum(ls)]
    for i in ls:
        res.append(res[-1] - i)
    return res


"""''
def parts_sums(ls):
    res = []
    length = len(ls) + 1
    for i in range(length):
        res.append(sum(ls[i:]))
    return res
""" ""
print(parts_sums([1, 2, 3, 4, 5, 6]))
