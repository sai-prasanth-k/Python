s = input()
s = s.lower()
s = s.replace(" ","")
s = s.replace("'","")
result = ""
for i in s :
    result = i + result
if s == result :
    print("True")
else :
    print("False")