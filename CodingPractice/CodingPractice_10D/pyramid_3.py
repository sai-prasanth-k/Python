n = int(input())
for i in range(n):
    stars ="* "*(i+1)
    print(stars)
for i in range(n):
    starsDown = "* "*(n-i-1)
    print(starsDown)