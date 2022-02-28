#  https://www.codewars.com/kata/511f11d355fe575d2c000001/train/python
def two_oldest_ages(ages):
    return [i for i in sorted(ages)[-2:]]


print(two_oldest_ages([1, 3, 10, 0]))
