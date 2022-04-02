#   https://www.codewars.com/kata/5656b6906de340bd1b0000ac


def longest(a1, a2):
    s = set()
    a3 = a1 + a2
    for i in a3:
        s.add(i)
    return "".join(sorted(i for i in s))


print(longest("aretheyhere", "yestheyarehere"))
