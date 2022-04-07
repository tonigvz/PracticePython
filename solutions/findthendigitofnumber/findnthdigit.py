#  https://www.codewars.com/kata/577b9960df78c19bca00007e
from multiprocessing.sharedctypes import Value


def findDigit(x, y):
    if y <= 0:
        return -1
    try:
        return str(abs(x))[-y]
    except IndexError:
        return 0


print(findDigit(-456, 4))
