m = int(input())
n = int(input())
count = 0
res = 0
for i in range(m,n+1) :
    count = len(str(i))
    res = res + count
print(res)