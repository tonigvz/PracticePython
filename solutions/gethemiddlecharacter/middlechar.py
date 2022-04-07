#  https://www.codewars.com/kata/56747fd5cb988479af000028
def getmiddle(x):
    length = int(len(x) / 2)
    if len(x) % 2 == 0:
        return x[length - 1 : length + 1]
    else:
        return x[length]


print(getmiddle("A"))
