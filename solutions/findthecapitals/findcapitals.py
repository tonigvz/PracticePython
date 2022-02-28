# https://www.codewars.com/kata/53573877d5493b4d6e00050c/train/python
def capital(capitals):
    res = []
    for d in capitals:
        if "country" in d:
            res.append(f"The capital of {d['country']} is {d['capital']}")
        else:
            res.append(f"The capital of {d['state']} is {d['capital']}")
    return res


state_capitals = [{"state": "Maine", "capital": "Augusta"}]
print(capital(state_capitals))
