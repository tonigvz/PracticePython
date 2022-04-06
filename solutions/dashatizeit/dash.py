#  https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python
def dashatize(n):
    print(n)
    if not isinstance(n, int):
        return "None"
    elif n < 0 and len(str(n)) == 1:
        return str(abs(n))
    else:
        n = abs(n)
        res = ""
        nlist = [int(i) for i in str(n)]
        for i, j in enumerate(nlist):
            if j % 2 == 0:
                res += f"{j}"
            else:
                try:
                    if (nlist[i + 1] % 2) != 0:
                        res += f"-{j}"
                    else:
                        res += f"-{j}-"
                except IndexError:
                    res += f"-{j}"
        return res if res[0] != "-" else res[1:]


print(dashatize(28369))
