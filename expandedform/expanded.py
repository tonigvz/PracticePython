# https://www.codewars.com/kata/5842df8ccbd22792a4000245
def expanded_form(num):
    rez = " + ".join([str(j + ("0" * i))[::-1]
                     for i, j in enumerate(str(num)[::-1]) if int(j) != 0])
    return rez[::-1]


print(expanded_form(12))
