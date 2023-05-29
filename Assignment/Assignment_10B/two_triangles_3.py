n = int(input())
for i in range (1,n+1):
    space = " "*(n-i)
    if i == 1:
        fspace = " "*(2*(n-i))
        firstRow=("* "*i)+fspace
        secondRow = fspace+("* "*i)
        print(firstRow+secondRow)
    elif i == n:
        firstRow1=("* "*n)+space
        secondRow1 = space+("* "*n)
        print(firstRow1+secondRow1)
    else:
        space = " "*(n-i)
        hollow = "  "*(i-2)
        firstTriangle="* "+hollow+"* "+space
        secspace = "   "*(n-i)
        secondTriangle = secspace+"* "+hollow+"* "
        print(firstTriangle+secondTriangle)