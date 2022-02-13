# https://www.codewars.com/kata/56f6ad906b88de513f000d96/train/python
def bonus_time(salary, bonus):
    return f"${salary}" if bonus == False else f"${salary*10}"


print(bonus_time(10000, True))
