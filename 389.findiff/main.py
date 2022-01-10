s =''
t ='y'
#method one
#print(set(s).symmetric_difference(set(t)))
#method two
for i in t:
    if s.count(i) != t.count(i):
        print(i)
#both work