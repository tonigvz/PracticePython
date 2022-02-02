# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
def is_isogram(string):
    s = string.lower()
    return sum(s.count(i) for i in s) == len(s)


print(is_isogram("Dermatoglyphics"))
