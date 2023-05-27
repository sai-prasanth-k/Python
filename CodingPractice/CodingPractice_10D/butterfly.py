n= int(input())
for i in range(1,n+1):
    stars = "* "*i
    spaces = "  "*(2*(n-i))
    print(stars+spaces+stars)
for i in range(1,n):
    starsDown = "* "*(n-i)
    spacesDown = "  "*(2*i)
    print(starsDown+spacesDown+starsDown)