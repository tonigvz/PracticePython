#  https://www.codewars.com/kata/57cf50a7eca2603de0000090/train/python
def move_ten(st):
    alph = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for i in st:
        res += alph[(alph.index(i) + 10) % len(alph)]
    return res


print(move_ten("testcase"))
