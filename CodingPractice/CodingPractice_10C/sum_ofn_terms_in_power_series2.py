x = int(input())
n = int(input())
res = 0
power = 2
for i in range (1,n+1) :
    ans = x ** power
    power = power + 2
    res = res + ans
print(res)