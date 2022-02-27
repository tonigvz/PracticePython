# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc
def factorial(n):
    res = 1
    if n < 0 or n > 12:
        raise ValueError("ValueError")
    else:
        for i in range(1, n + 1):
            res *= i
        return res


print(factorial(15))
