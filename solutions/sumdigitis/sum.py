# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def digital_root(n):
    c = sum(int(i) for i in str(n))
    if len(str(c)) >= 2:
        c = digital_root(c)
    return c


print(digital_root(942))
