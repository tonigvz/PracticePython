# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
def find_short(s):
    length = [len(i) for i in s.split()]
    return(min(length))


print(find_short("bitcoin take over the world maybe who knows perhaps"))
