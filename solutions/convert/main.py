# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
def digitize(n):
    result = []
    rev = str(n)[::-1]
    print(rev)
    for i in rev:
        result.append(int(i))
    return result


n = 1234
digitize(n)
