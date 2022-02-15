# https://www.codewars.com/kata/591cac98a6007e87d900013a
# capitalize first letter of first word
def toSentenceCase(s):
    return s.capitalize()


# lowercase every letter
def toLowerCase(s):
    return s.lower()


# uppercase every later
def toUpperCase(s):
    return s.upper()


# capitalize first letter in each word
def capitalizeEachWord(s):
    return s.title()


# uppercase letter change to lowercase annd lowercase to uppercase
def toToggleCase(s):
    res = ""
    for i in s:
        if i.islower():
            res += i.upper()
        else:
            res += i.lower()
    return res


print(toToggleCase("heLLo woRld"))
