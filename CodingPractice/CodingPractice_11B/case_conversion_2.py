s = input()
n = len(s)
result = ""
for i in range(0,n):
    each_character = s[i]
    upper_case = s[i].upper()
    if each_character == upper_case :
        result = result + "-" + s[i]
    else :
        result = result + s[i]
print(result.lower())