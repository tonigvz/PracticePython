#  https://www.codewars.com/kata/56b8903933dbe5831e000c76/train/python
def spoonerize(words):
    txt = words.split()
    length = len(txt)
    first_word = txt[length - 1][0] + txt[0][1:]
    second_word = txt[0][0] + txt[length - 1][1:]
    txt[0] = first_word
    txt[length - 1] = second_word
    return " ".join(txt)


print(spoonerize("nit picking"))
