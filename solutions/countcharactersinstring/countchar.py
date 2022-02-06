# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
def count(string):
    return dict((i, string.count(i)) for i in string)

    #from collections import Counter
    # def count(string):
    #    return Counter(string)


count('aba')
