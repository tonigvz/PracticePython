#  https://www.codewars.com/kata/594adadee075005308000122/train/python
def even_and_odd(n):
    ne = ""
    no = ""
    for i in str(n):
        if int(i) % 2 == 0:
            ne += i
        else:
            no += i
    if ne and no:
        return (int(ne), int(no))
    elif not ne:
        return (0, int(no))
    else:
        return (int(ne), 0)
