#  https://www.codewars.com/kata/56541980fa08ab47a0000040
def printer_error(s):
    good = "abcdefghijklm"
    res = ""
    for i in s:
        if i not in good:
            res = res + i
    return f"{len(res)}/{len(s)}"


print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
