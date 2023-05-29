n = int(input())
space = "  "*(n-1)
print(space+"1 ")
for i in range (2,n+1):
    space = "  "*(n-i)
    hollow = "  "*(i-2)
    print(space+(str(i)+" ")+hollow+(str(i)+" "))
    
for i in range (1,n):
    space = "  "*(i)
    if i == (n-1):
        print(space+"1")
    else :
        hollow = " "*((2*n)-(2*i)-3)
        # hollow = "  "*(n-i-3)
        print(space+str(n-i)+hollow+str(n-i))