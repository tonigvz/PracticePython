# https://www.codewars.com/kata/56606694ec01347ce800001b/train/python
def is_triangle(a, b, c):
    l = [a, b, c]
    sort = sorted(l)
    return sort[0] + sort[1] > sort[2]


print(is_triangle(7, 2, 2))
