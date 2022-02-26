# https://www.codewars.com/kata/544aed4c4a30184e960010f4
def divisors(integer):
    # list with all divisors , is divisor if integer modul i is 0
    res = [i for i in range(2, integer) if (integer % i) == 0]
    # if the len of the list with divisors is 0 print integer is prime else list
    return f"{integer} is prime" if len(res) == 0 else res


print(divisors(24))
