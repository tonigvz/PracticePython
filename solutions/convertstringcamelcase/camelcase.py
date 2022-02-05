# https://www.codewars.com/kata/517abf86da9663f1d2000003
def to_camel_case(text):
    s = text.split('-')
    if s[0].istitle():
        return ''.join(s)
    else:
        for i in range(len(s)):
            if i == 0:
                continue
            else:
                s[i] = s[i].capitalize()

    res = "".join(i for i in s)
    return res


print(to_camel_case("the-Stealth-Warrior"))
