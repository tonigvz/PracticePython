#  https://www.codewars.com/kata/5601409514fc93442500010b/train/python
def better_than_average(class_points, your_points):
    points_average = sum([i for i in class_points]) / len(class_points)
    return your_points > points_average


print(better_than_average([2, 3], 5))
