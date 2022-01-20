def likes(names):
    length = len(names) 
    if length == 0:
        string = 'no one likes this'
    elif length == 1:
        string = names[0]+ ' likes this'
    elif length == 2:
        string = names[0]+ ' and ' +names[1]+ ' like this'
    elif length == 3:
        string = names[0]+', '+names[1]+' and '+names[2]+' like this'
    elif length > 3:
        string = names[0]+', '+names[1]+' and '+str(length-2)+' others like this'
    return string
    

names = ['john','peter']
print(likes(names))