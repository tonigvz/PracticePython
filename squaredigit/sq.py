
num = 9119
strnum = str(num)
x = 0
result = ""
for i in strnum:
    x += int(i)**2
    result += str(x)
    x = 0
print(int(result))
