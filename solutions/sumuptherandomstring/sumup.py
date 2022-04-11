#  https://www.codewars.com/kata/55da6c52a94744b379000036
import re


def sum_of_string(n):
    res = re.findall(r"\d+(?:\d+)?", n)
    return sum(int(i) for i in res)


print(sum_of_string("in 2015, i want to know how much does iphone 6+ cost? 3.15"))
