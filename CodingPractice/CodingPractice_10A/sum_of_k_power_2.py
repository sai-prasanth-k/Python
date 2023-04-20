n = int(input())
i = 0 
m = str(n)
length = len(m)
result = 0
while i < length:
    result = result + (int(m[i])**length)
    i = i + 1
print(result)
    