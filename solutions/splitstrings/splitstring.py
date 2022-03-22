#   https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
def solution(s):
    res = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            res.append(s[i] + s[i + 1])
        else:
            res.append(s[i] + "_")
    return res
    # list comprehension
    """
    return [
        (s[i] + s[i + 1]) if i + 1 < len(s) else (s[i] + "_")
        for i in range(0, len(s), 2)
    ]
    """


print(solution("abc"))
