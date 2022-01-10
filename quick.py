temp = x
reverse = 0
while temp:
    last = temp % 10
    reverse = reverse * 10 + last
    temp = temp // 10
if x == reverse:
    print("true")
else:
    print("false")
