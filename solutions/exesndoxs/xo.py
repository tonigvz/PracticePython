# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
def xo(s):
    cx = sum(1 for i in s.lower() if i == 'x')
    co = sum(1 for i in s.lower() if i == 'o')
    return True if cx == co else False


print(xo('xo0'))
