x = int(input())
n = int(input())
i = 1 
result = 1
while i <= n :
    result = result * (x+1)
    x = x + 1
    i = i + 1
print(result)