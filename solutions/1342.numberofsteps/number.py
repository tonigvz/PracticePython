#  https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
def numberOfSteps(num: int) -> int:
    res = num
    count = 0
    while res > 0:
        if res % 2 == 0:
            res /= 2
            count += 1
        else:
            res -= 1
            count += 1
    return count


num = 14
print(numberOfSteps(num))
