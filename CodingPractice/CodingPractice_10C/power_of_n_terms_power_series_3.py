x = int(input())
n = int(input())
power = 2
res = 0
res1 = 0
for i in range(1,n+1) :
    ans = x ** power
    if power % 4 == 0 :
        res = res + ans
    else :
        res1 = res1 - ans
    power = power + 2
total =-1*(res + res1)
print(total)