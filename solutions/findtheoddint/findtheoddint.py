# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
def find_it(seq):
    count = dict((i, seq.count(i)) for i in seq)
    for key, value in count.items():
        if value % 2 != 0:
            return key


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
