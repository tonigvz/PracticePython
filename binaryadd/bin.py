# https://www.codewars.com/kata/551f37452ff852b7bd000139
def add_binary(a, b):
    c = a + b
    return bin(c)[2:]


a = 1
b = 1
print(add_binary(a, b))
