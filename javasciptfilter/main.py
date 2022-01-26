# https://www.codewars.com/kata/514a6336889283a3d2000001
def get_even_numbers(arr):
    n = arr

    def check_even(n):
        if n % 2 == 0:
            return True
        return False

    even_number = filter(check_even, arr)
    even_numbers = list(even_number)

    return even_numbers


arr = [2, 4, 5, 6]
print(get_even_numbers(arr))
