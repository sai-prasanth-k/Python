s = input()
result = ""
s = s.lower()
length = len(s)
for i in s :
    result = i + result
if result == s :
    print("Palindrome")
else :
    print("Not a Palindrome")