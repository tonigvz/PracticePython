#  https://www.codewars.com/kata/52c31f8e6605bcc646000082
def two_sum(n, target):
    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            if n[i] + n[j] == target:
                return [i, j]
