# https://www.codewars.com/kata/554ca54ffa7d91b236000023


def delete_nth(data, n):
    # created empty list
    res = []
    # iterating through data
    for i in data:
        # if count of i is bigger than n append to res
        if res.count(i) < n:
            res.append(i)
    # return res
    return res


print(delete_nth([20, 37, 20, 21], 1))
