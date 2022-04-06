#  https://www.codewars.com/kata/5aa3af22ba1bb5209f000037/train/python
import re


def solve(eq):
    return "".join(
        s if s.isdigit() else s[::-1] for s in reversed(re.split("(\d+)", eq))
    )


print(solve("c*33-g-z+e+41*x*d*i*67-w-29-93*s/17/p+z+r"))
