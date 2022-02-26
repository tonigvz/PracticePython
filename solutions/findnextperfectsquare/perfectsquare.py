# https://www.codewars.com/kata/56269eb78ad2e4ced1000013
import math


def find_next_square(sq):
    # get root of perfect square
    root = int(math.sqrt(sq))
    # check if root^root is equal to sq
    if root * root == sq:
        # add one to root and return next perfect square
        root += 1
        return root * root
    else:
        return -1


print(find_next_square(151))
