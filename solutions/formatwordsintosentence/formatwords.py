#  https://www.codewars.com/kata/51689e27fe9a00b126000004/train/python
def format_words(words):
    if not words or words == [""]:
        return ""
    words = [i for i in words if i != ""]
    if len(words) == 1:
        return words[0]
    return ", ".join(words[:-1]) + " and " + words[-1]


print(format_words(["one0", "two", "thrre", "four", "five", "six", "seve", "eight"]))
