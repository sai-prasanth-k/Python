n = int(input())
for i in range(1,n+1):
    firststar = "* "*i
    firstspaces = "  "*(n-i)
    firstTriangle = firststar + firstspaces
    
    secondspaces = "  "*(n-i)
    secondstar = "* "*i
    secondTriangle = secondspaces + secondstar
    
    triangle = firstTriangle + secondTriangle
    
    print(triangle)