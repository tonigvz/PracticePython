# https://www.codewars.com/kata/55c45be3b2079eccff00010f
def order(sentence):
    digits = sentence.split()
    res = ['' for i in digits]
    for i in digits:
        for j in i:
            if j.isdigit():
                res[int(j)-1] = i

    return " ".join(res)


print(order("is2 Thi1s T4est 3a"))
