n = int(input())
for i in range(1,n+1):
    numbers = (str(i)+" ")*i
    spaces = " "*(n-i)
    print(spaces+numbers)
for i in range(1,n):
    numbers = (str(n-i)+" ")*(n-i)
    spaces = " "*i
    print(spaces+numbers)