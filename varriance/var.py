vac_nums = [0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3
            ]
thesum = sum(vac_nums)  # the sum of the list
mean = thesum/len(vac_nums)  # mean

diff = [(x-mean)**2 for x in vac_nums]  # squared differences from the mean

print(sum(diff)/len(diff))  # the variance
