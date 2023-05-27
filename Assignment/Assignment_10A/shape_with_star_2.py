n = int(input())
print("* "*((2*n)-1))
for i in range(1,n+1):
    firststars = "* "*(n-i)
    firstspaces = " "*i
    first = firstspaces+firststars
    spaceBtn = " "*(i-1)
    secondstars = "* "*(n-i)
    secondspaces = " "*(i-1)
    second = secondspaces+secondstars
    print(first+spaceBtn+second)