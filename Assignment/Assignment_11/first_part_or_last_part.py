s1 = input()
s2 = input()
count = 0
length1 = len(s1)
length = len(s2)
start = length1-length
for i in range (length) :
    if s1[i] == s2[i] or s1[start+i] == s2[i]:
        count = count + 1
if count == length :
    print(True)
else :
    print(False)