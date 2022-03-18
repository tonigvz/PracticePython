#  https://www.codewars.com/kata/57741d8f10a0a66915000001/train/python
def int_diff(lst, n):
    c = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if abs(lst[j] - lst[i]) == n:
                c += 1

    return c


print(int_diff([1, 1, 1, 1], 0))
