temp = x
reverse = 0
while temp > 0:
    last = temp % 10
    reverse = reverse * 10 + last
    temp //= 10
return x == reverse
