a = int(input())
res = str(a)
lenres = len(res)
ans = 0
for i in range(lenres) :
    ans = ans + int(res[i])
print(ans)