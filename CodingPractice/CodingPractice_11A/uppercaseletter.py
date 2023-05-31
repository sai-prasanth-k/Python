s = input()
i = 0 
res = ""
while (i < len(s)) :
    if s[i].isupper() :
        res = res + s[i]
    i = i +1
print(res)