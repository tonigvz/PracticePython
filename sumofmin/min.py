# https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python
def sum_of_minimums(x):
    sum = 0
    for i in range(len(x)):
        sum += min(x[i])
    print(sum)


(sum_of_minimums([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [20, 21, 34, 56, 100]]))
