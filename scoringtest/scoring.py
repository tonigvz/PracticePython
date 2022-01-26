# https://www.codewars.com/kata/55d2aee99f30dbbf8b000001
# returns test score
def score_test(tests, right, omit, wrong):
    countr = 0
    counto = 0
    countw = 0
    for i in tests:
        if i == 0:
            countr += 1
        elif i == 1:
            counto += 1
        else:
            countw += 1
    result = (countr * right) + (counto * omit) - (countw * wrong)
    return result


tests = [0, 0, 0, 0, 2, 1, 0]
right = 2
omit = 0
wrong = 1

print(score_test(tests, right, omit, wrong))
