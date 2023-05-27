n = int(input())
for i in range(1,n+1):
    stars = "* "*(n-i+1)
    spaces = "  "*(i-1)
    print(spaces+stars)