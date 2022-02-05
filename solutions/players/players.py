import math
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

mean = sum(players)/len(players)
print("the mean is:", mean)
diff = [(x-mean)**2 for x in players]
var = sum(diff)/len(diff)
print("the variance is:", var)
std = math.sqrt(var)
print("the standard deviation is :", std)
low = mean-std
high = mean+std
count = 0
player_match = []
for x in players:
    if low < x < high:
        count = count+1
        player_match.append(x)
print("number of players that match:", count)
print("the heights that match are:", player_match)
