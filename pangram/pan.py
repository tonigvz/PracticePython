# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
import string


def pan(str):
    alph = "abcdefghjklmnopqrstuvwxyz"
    for i in alph:
        if i not in str.lower():
            return False
    return True


string = "This isn't a pangram!"
print(pan(string))
