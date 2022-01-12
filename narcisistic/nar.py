value = 153
n = len(str(value))
nar = 0 
for i in str(value):
    nar += int(i)**n
print(nar)
if nar == value:
    print("True")
else:
    print("False") 
