# https://www.codewars.com/kata/525f50e3b73515a6db000b83
def create_phone_number(n):
    txt = "".join(str(i) for i in n)
    return f"({txt[:3]}) {txt[3:6]}-{txt[6:]}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
