#  https://www.codewars.com/kata/59ad7d2e07157af687000070/train/python
def sentencify(words):
    res = words[0].capitalize() if words[0].islower() else words[0]
    for i in range(1, len(words)):
        res += " "
        res += words[i]
    return f"{res}."


print(sentencify(["i", "am", "an", "AI"]))
