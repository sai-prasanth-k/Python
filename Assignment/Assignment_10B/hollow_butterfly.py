n = int(input())
for i in range (1,n+1):
    if i == 1 :
        spaces = " "*(2*(n-i))
        firstRow = ("* "*i)+spaces
        secondRow = spaces+("* "*i)
        print(firstRow+secondRow)
    else :
        spaces = " "*(n-i)
        hollow = "  "*(i-2)
        firstTriangle = "* "+hollow+"* "+spaces
        sspaces = "   "*(n-i)
        secondTriangle = sspaces+"* "+hollow+"* "
        print(firstTriangle+secondTriangle)
        
for i in range(0,n):
    if i == n-1:
        spaces = " "*((2*n-2)*(n-i))
        lastRow = ("* ")+spaces
        lastRow1 = spaces+("* ")
        print(lastRow+lastRow1)
    else :
        spaces = " "*(2*i)
        hollow = "  "*(n-i-2)
        firstTriangle = "* "+hollow+"* "+spaces
        secondTriangle = spaces+"* "+hollow+"* "
        print(firstTriangle+secondTriangle)