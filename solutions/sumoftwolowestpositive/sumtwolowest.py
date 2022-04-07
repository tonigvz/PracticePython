#  https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
def sum_two_smallest_numbers(numbers):
    listsort = sorted(numbers)
    return listsort[0] + listsort[1]


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
