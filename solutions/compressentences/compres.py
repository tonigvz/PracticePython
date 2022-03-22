#  https://www.codewars.com/kata/59de469cfc3c492da80000c5
def compress(sentence):
    txt = (sentence.lower()).split()
    res = []
    for i in txt:
        if i not in res:
            res.append(i)
    return "".join([str(res.index(i)) for i in txt])


print(compress("The number 0 is such a strange number Strangely it has zero meaning"))
