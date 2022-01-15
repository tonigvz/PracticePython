list = [1, 2, 'a', 'b']
slist = []
llist = []
for i in list:
    if isinstance(i, int):
        slist.append(i)

print(slist)
