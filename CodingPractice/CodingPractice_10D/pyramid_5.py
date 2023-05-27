n = int(input())
for i in range (1,n+1):
    space = "  "*(n-i)
    symbol = "+ "*(i-1)+"# "
    print(space+symbol)
for i in range (1,n):
    space = "  "*i
    symbolDown = "+ "*((n-i)-1) + "# "
    print(space+symbolDown)