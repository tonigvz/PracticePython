#  https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python
def in_array(array1, array2):
    res = set()
    for i in array1:
        for j in array2:
            if i in j:
                res.add(i)
    return sorted(list(res))


a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
