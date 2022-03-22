#  https://www.codewars.com/kata/595519279be6c575b5000016
def battle(x, y):
    alph = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    score1 = sum([alph.index(i) + 1 for i in x])
    score2 = sum([alph.index(i) + 1 for i in y])
    if score1 > score2:
        return x
    elif score1 < score2:
        return y
    else:
        return "Tie!"


print(battle("FOUR", "FIVE"))
