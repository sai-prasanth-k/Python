n = int(input())
for i in range(1,n+1):
    spaces = " "*(n-i)
    stars = "* "*i
    print(spaces+stars)

for i in range(1,n):
    if i == n-1 :
        spaces = " "*((n-1)*(n-i))
        print(spaces+"* ")
    else:
        spaces = " "*i
        hollow = "  "*(n-i-2)
        print(spaces+"* "+hollow+"* ")