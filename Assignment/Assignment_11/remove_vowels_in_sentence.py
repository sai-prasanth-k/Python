s = input()
vowel = {'a','e','o','u','i'}
for i in s :
    if i.lower() in vowel :
        s = s.replace(i,"")
print(s)