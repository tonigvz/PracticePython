list = [1, 2, "a", "b"]
slist = []
for i in list:
    if isinstance(i, int):
        slist.append(i)

print(slist)
