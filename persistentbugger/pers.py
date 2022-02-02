# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
def persistence(n):
    def mul(n):
        c = 1
        for i in str(n):
            c *= int(i)
        return c

    count = 0
    while n // 10 > 0:
        n = mul(n)
        count += 1
    return count


print(persistence(999))
