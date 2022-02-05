# https://www.codewars.com/kata/54edbc7200b811e956000556
def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count


array1 = [True,  True,  True,  False,
          True,  True,  True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True,  True]

print(count_sheeps(array1))
