#  https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python
def vowel_indices(n):
    res = []
    vowels = "aeiouyAEIOUY"
    for i, j in enumerate(n):
        if j in vowels:
            res.append(i + 1)
    return res


print(vowel_indices("super"))
