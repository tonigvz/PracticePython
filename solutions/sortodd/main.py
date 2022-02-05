#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
def sort_array(source):
    odd = sorted([n for n in source if n%2!=0])
    res = []
    c = 0
    for i in source:
        if (i % 2) != 0:
            res.append(odd[c])
            c += 1
        else:
            res.append(i)
    return res
        

source = [7,1,2]
print(sort_array(source))
