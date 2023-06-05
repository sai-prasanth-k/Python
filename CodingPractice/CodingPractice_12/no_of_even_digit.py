n = int(input())
s = str(n)
length = len(s)
count = 0
for i in range(length):
    c = int(s[i])
    if c % 2 == 0 :
         count = count + 1
if count > 2 :
    print("Count of even digits is greater than two")
else :
    print("Count of even digits is not greater than two")