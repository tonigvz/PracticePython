#  https://www.codewars.com/kata/534d0a229345375d520006a0/train/python
def power_of_two(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True


print(power_of_two(16))
