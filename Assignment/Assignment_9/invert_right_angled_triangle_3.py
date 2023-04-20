n = int(input())
print("* "*n)
for i in range(n+1) :
    result = "+ " * (n-1 - i)
    print(result)