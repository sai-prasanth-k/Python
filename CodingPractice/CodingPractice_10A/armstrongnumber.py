n = int(input())
m = str(n)
length = len(m)
i = 0
result = 0
while i < length :
    result = result + (int(m[i])** length)
    i = i + 1
if result == n :
    print("Armstrong Number")
else :
    print("Not an Armstrong Number")