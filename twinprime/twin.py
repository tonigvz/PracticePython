# https://www.codewars.com/kata/59b7ae14bf10a402d40000f3/train/python


def prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


def is_twinprime(n):
    less = n - 2
    m = n + 2
    if prime(n):
        if prime(m) | prime(less):
            return True
        else:
            return False
    else:
        return False


n = 5
print(is_twinprime(n))
