#  https://www.codewars.com/kata/559e5b717dd758a3eb00005a/train/python
def drop_cap(str_):
    return " ".join(i.title() if len(i) > 2 else i for i in str_.split(" "))


print(drop_cap("one  space"))
