# https://www.codewars.com/kata/53573877d5493b4d6e00050c/train/python
def capital(capitals):
    for i in capitals:
        print("the capital of ", i["state"], " is", i["capital"])


state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
print(capital(state_capitals))
