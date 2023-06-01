s = input()
length = len(s)
result_s = s[0]
for i in range(1,length):
    character = s[i]
    upper_case = character.upper()
    
    if character == upper_case :
        result_s = result_s + " " + character
    else :
        result_s = result_s + character
        
print(result_s)