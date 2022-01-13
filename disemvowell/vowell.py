data = "This website is for losers LOL!"
vowels = "aeiou"
result = data
for i in vowels:
    result = result.replace(i, '')

print(result)    
