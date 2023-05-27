n = int(input())
for i in range(1,n+1):
    stars = "* "*(i)
    spaces = " "*(n-i)
    print(spaces+stars)
for i in range(1,n+1):
    stars= "* "*(n-i)
    spaces = " "*(i)
    print(spaces+stars)