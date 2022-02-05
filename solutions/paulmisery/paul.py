# https://www.codewars.com/kata/57ee31c5e77282c24d000024/train/python
def paul(x):
    kata, Petes_kata, life, eating = 5, 10, 0, 1
    countl, counte, countk, countp = 0, 0, 0, 0
    for i in x:
        countl = x.count("life")
        counte = x.count("eating")
        countk = x.count("kata")
        countp = x.count("Petes kata")
    sum = ((countl * life) + (counte * eating) +
           (countk * kata) + (countp * Petes_kata))
    if sum < 40:
        return 'Super happy!'
    elif sum < 70 >= 40:
        return 'Happy!'
    elif sum < 100 >= 70:
        return 'Sad!'
    else:
        return 'Miserable!'


print(paul(['life', 'eating', 'life']))
