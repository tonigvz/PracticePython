#  https://www.codewars.com/kata/58e09234ca6895c7b300008c
def palindrom_num(num, s):
    if type(num) != int or num < 0:
        return "Not valid"
    if type(s) != int or s < 0:
        return "not valid"
    res = []
    while len(res) < s:
        if num >= 10 and str(num) == str(num)[::-1]:
            res.append(int(num))
        num += 1
    return res


print(palindrom_num(6, 4))
