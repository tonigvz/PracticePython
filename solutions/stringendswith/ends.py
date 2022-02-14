# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
def solution(string, ending):
    return True if ending in string[-len(ending) :] else False


print(solution("fails", "ails"))
