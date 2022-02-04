# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    res = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            res.append(i)

    return sum(res)


print(solution(10))
