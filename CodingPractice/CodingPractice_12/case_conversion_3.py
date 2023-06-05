s = input()
n = len(s)
result = s[0]
for i in range(1,n):
    character = s[i]
    uppercase = character.upper()
    
    if character == uppercase :
        result = result + "-" + character
    else :
        result = result + character

print(result.lower())