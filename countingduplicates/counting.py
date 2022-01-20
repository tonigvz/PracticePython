#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
def duplicate_count(text):
    duplicates = 0
    text = text.lower()
    for c in set(text):
        if text.count(c) > 1:
            duplicates += 1
    return duplicates