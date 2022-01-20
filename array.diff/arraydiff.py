#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
a = [1,2,2,2,3]
b = [2]
res = []
def array_diff(a,b):
    for i in a:
        if i in b:
            pass
        else:
            res.append(i)
    return res
    #return [i for i in a if i not in b]

print(array_diff(a,b))
    