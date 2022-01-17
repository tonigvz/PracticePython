# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    sres = sentence.split(" ")
    for i in range(len(sres)):
        if len(sres[i]) > 4:
            sres[i] = sres[i][::-1]
    return ' '.join(sres)
