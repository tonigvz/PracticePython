#   https://www.codewars.com/kata/5921c0bc6b8f072e840000c0/train/python


def sequence_classifier(L):
    strin = all(x < y for x, y in zip(L, L[1:]))
    notde = all(x <= y for x, y in zip(L, L[1:]))
    strde = all(x > y for x, y in zip(L, L[1:]))
    notin = all(x >= y for x, y in zip(L, L[1:]))
    const = all(x == y for x, y in zip(L, L[1:]))
    if strin:
        return 1
    elif const:
        return 5
    elif strde:
        return 3
    elif notin:
        return 4
    elif notde:
        return 2
    else:
        return 0

    # another solution
    """
    if all(arr[i] == arr[i+1] for i in range(len(arr)-1)): return 5
    if all(arr[i] <  arr[i+1] for i in range(len(arr)-1)): return 1
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)): return 2
    if all(arr[i] >  arr[i+1] for i in range(len(arr)-1)): return 3
    if all(arr[i] >= arr[i+1] for i in range(len(arr)-1)): return 4
    return 0
    """


print(sequence_classifier([8, 8, 8, 8]))
