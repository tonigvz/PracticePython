# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
import enum


def find_needle(haystack):
    return "".join("found the needle at position "+str(i) for i, j in enumerate(haystack) if j == "needle")


print(find_needle(['3', '123124234', None, 'needle',
                   'world', 'hay', 2, '3', True, False]))
