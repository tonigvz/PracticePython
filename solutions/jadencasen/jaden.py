# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
    n = [i.capitalize() for i in string.split()]
    return " ".join(n)


quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))
