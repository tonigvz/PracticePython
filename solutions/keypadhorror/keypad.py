#  https://www.codewars.com/kata/5572392fee5b0180480001ae/train/python
def computer_to_phone(numbers):
    tans = str.maketrans("789456123", "123456789")
    res = str(numbers).translate(tans)
    return res


print(computer_to_phone(789))
