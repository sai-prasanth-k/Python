n = int(input())
result = 0
for i in range(1,n) :
    if n % i == 0 :
        result = result + i
if result == n :
    print("Perfect Number")
else :
    print("Not a Perfect Number")