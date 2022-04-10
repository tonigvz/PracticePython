#   https://www.codewars.com/kata/597bb84522bc93b71e00007e/train/python
def string_merge(string1, string2, letter):
    return string1[: string1.index(letter)] + string2[string2.index(letter) :]


print(string_merge("hello", "world", "l"))
