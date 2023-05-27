n = int(input())
nstr = str(n)
nlen = len(nstr)
count = 0
res = 0
for i in range(1,n+1):
    count = len(str(i))
    res = res + count
print(res)