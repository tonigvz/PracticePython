#  https://www.codewars.com/kata/55f2b110f61eb01779000053
def get_sum(a, b):
    # turn a,b into tuple
    l = (a, b)
    # sort it
    t = sorted(l)
    # return sum
    return sum(i for i in range(t[0], (t[1] + 1)))


print(get_sum(0, 1))
