# https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python
def flatten_and_sort(array):
    return sorted([j for i in array for j in i])


print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))
