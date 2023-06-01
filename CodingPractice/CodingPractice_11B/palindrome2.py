s = input()
d = s.lower()
reverse = ""
for i in d :
    reverse = i + reverse
print(d == reverse)