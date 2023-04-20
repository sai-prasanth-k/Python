n = int(input())
k = int(input())
result = 0
for i in range(n+1) :
    result = result + (i ** k)
print(result)