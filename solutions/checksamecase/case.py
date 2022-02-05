# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b
def same_case(a, b):
    return a.isupper() == b.isupper() or a.islower() == b.islower() if a.isalpha() and b.isalpha() else -1


print(same_case('A', '?'))
