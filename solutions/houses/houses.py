import numpy as np

data = np.array(
    [
        150000,
        125000,
        320000,
        540000,
        200000,
        120000,
        160000,
        230000,
        280000,
        290000,
        300000,
        500000,
        420000,
        100000,
        150000,
        280000,
    ]
)

low = np.mean(data) - np.std(data)
high = np.mean(data) + np.std(data)
count = 0
for x in data:
    if low < x < high:
        count = count + 1
print(count * 100 / data.size)
