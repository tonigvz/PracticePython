#  https://www.codewars.com/kata/5900750cb7c6172207000054
def sticky_calc(operation, val1, val2):
    first = str(round(val1)) + str(round(val2))
    return round(eval(first + operation + str(round(val2))))


print(sticky_calc("/", 51, 63))
