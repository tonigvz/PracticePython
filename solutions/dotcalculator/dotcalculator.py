#  https://www.codewars.com/kata/6071ef9cbe6ec400228d9531/train/python
def calculator(txt):
    res = txt.split()
    if res[1] == "+":
        op = res[0].count(".") + res[2].count(".")
        return op * "."
    elif res[1] == "-":
        op = res[0].count(".") - res[2].count(".")
        return op * "."
    elif res[1] == "*":
        op = res[0].count(".") * res[2].count(".")
        return op * "."
    elif res[1] == "//":
        op = res[0].count(".") // res[2].count(".")
        return op * "."


print(calculator("..... - ..."))
