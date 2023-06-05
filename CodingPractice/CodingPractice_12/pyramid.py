n = int(input())

k = n
for i in range(1, n+1):
    spaces = " " * (k-1)
    stars = "* " * i
    print(spaces+stars)
    k = k - 1
