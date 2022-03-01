#  https://www.codewars.com/kata/5803c0c6ab6c20a06f000026/train/python
def swap_vowel_case(st):
    vowels = "aeouiAEOUI"
    res = ""
    for i in st:
        if i not in vowels:
            res = res + i
        else:
            res = res + i.swapcase()
    return res


swap_vowel_case("C is alive!")
