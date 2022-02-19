# https://www.codewars.com/kata/58039f8efca342e4f0000023/python


def changer(s):
    return s.lower().translate(
        str.maketrans("abcdefghijklmnopqrstuvwxyz", "bcdEfghIjklmnOpqrstUvwxyzA")
    )


print(changer("Cat30"))
