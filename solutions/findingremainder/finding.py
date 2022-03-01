#  https://www.codewars.com/kata/564f458b4d75e24fc9000041/train/python
def remainder(dividend, divisor):
    while dividend >= divisor:
        dividend -= divisor
    return dividend


print(remainder(409, 408))
