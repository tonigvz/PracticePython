s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
r = list(s)
j = 0
for i in indices:
    r[i] = s[j]
    j += 1
print("".join(r))
