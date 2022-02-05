# https://leetcode.com/problems/sorting-the-sentence/
def sorting(string):
    dict = {}
    txt = string.split()
    res = ""
    for i in txt:
        dict[i[-1]] = i[:-1]
    for i in sorted(dict):
        res = res + "".join(dict[i]) + " "

    return res[:-1]


print(sorting("is2 sentence4 this1 a3"))
