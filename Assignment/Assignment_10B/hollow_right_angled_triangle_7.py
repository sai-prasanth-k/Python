n = int(input())
print("+ "*n)
for i in range (1,n):
    if i == n-1:
        print("  "*(n-1)+"*")
    else:
        space = "  "*(i)
        hollow = "  "*(n-i-2)
        print(space+"* "+hollow+"* ")