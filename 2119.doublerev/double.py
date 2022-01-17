#https://leetcode.com/problems/a-number-after-a-double-reversal/
def reverse(x):
    y =  str(x)
    y =  y[::-1]
    y = int(y)
    return y

num = 526
reversed1 = reverse(num)
print(reversed1)
reversed2 = reverse(reversed1)
print(reversed2)
if num == reversed2:
    print("true")