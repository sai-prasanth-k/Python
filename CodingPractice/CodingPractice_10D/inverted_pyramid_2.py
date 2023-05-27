n = int(input())
for i in range(n):
    stars = "* "*(n-i)
    spaces = " "*i
    print(spaces+stars)