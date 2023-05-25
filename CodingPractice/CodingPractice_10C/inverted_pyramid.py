n = int(input())
for i in range(n):
    stars = "*"*(2*(n-i)-1)
    spaces = " "*i
    print(spaces+stars)