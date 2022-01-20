#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
a = [1,2,2,2,3]
b = [2]
def array_diff(a,b):
    res = []
    for i in a:
        if i not in b:
            res.append(i)
    return res
    #return [i for i in a if i not in b]

print(array_diff(a,b))
    