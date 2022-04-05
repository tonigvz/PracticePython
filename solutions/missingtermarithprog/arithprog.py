#  https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python
def find_missing(ls):
    sumn = ((len(ls) + 1) / 2) * (ls[0] + ls[len(ls) - 1])
    slist = sum(ls)
    return sumn - slist


print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))
