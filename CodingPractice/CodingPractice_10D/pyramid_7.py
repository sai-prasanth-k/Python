n = int(input())
for i in range(1,n+1):
    numbers = (str(i)+" ")*i
    spaces = " "*(n-i)
    print(spaces+numbers)