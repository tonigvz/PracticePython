# https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python


def fake_bin(x):
    r = ""
    for i in x:
        if i >= "5":
            r += "1"
        else:
            r += "0"
    print(r)


x = "45385593107843568"
fake_bin(x)
