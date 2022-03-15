#  https://www.codewars.com/kata/57f75cc397d62fc93d000059
def calc(x):
    total1 = "".join(str(ord(i)) for i in x)
    total2 = total1.replace("7", "1")
    res2 = [int(i) for i in str(int(total1) - int(total2))]
    return res2.count(6) * 6


print(calc("ifkhchlhfd"))
