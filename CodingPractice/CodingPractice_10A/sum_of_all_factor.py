n = int(input())
result = 0
i = 1 
while i <= n :
    if n % i == 0 :
        result = result + i 
    i = i + 1 
print(result)