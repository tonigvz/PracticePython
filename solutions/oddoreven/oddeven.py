# https://www.codewars.com/kata/5949481f86420f59480000e7
def odd_or_even(arr):
    return "even" if ((sum(i for i in arr)) % 2) == 0 else "odd"


print(odd_or_even([0, 1, 2]))
