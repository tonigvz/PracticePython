#  https://www.codewars.com/kata/58ba6fece3614ba7c200017f/train/python
def palindrome(num):
    if type(num) != int or num != abs(num):
        return "Not valid"
    return True if str(num) == str(num)[::-1] else False


print(palindrome(1221))
