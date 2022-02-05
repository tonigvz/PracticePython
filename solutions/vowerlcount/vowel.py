# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
def get_count(sentence):
    vowels = "aeiou"
    count = (sum([1 for i in sentence if i in vowels]))
    return count


str = "a"
print(get_count(str))
