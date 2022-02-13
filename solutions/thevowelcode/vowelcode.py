# https://www.codewars.com/kata/53697be005f803751e0015aa
def encode(st):
    en = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    for i in en:
        st = st.replace(i, en[i])
    return st


def decode(st):
    de = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    for i, j in de.items():
        st = st.replace(j, i)
    return st


print(decode("h2ll4"))
