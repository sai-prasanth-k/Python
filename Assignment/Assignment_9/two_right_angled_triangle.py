n = int(input())
for i in range(1,n+1) :
    result = "* "*i
    print(result)
for j in range(n+1) :
    ans = "* " * (n - j) 
    print(ans)