# https://www.codewars.com/kata/5809c661f15835266900010a


def double_every_other(lst):
    for i in range(len(lst)):
        if i % 2 != 0:
            lst[i] *= 2
    print(lst)


double_every_other([1, 2, 3, 4, 5])
