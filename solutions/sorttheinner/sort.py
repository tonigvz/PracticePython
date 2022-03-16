#  https://www.codewars.com/kata/5898b4b71d298e51b600014b/train/python
def sort_the_inner_content(words):
    r = words.split()
    q = ""
    for i in r:
        res = i[1 : len(i) - 1]
        q += i.replace(res, "".join(sorted(res, reverse=True)))
        q += " "
    return q[:-1]


print(sort_the_inner_content("sort the inner content in descending order"))
