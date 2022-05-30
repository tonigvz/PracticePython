def is_narcissistic(n):
    sum = 0
    for i in str(n):
        sum += int(i) ** len(str(n))
    return sum == n


print(is_narcissistic(153))
