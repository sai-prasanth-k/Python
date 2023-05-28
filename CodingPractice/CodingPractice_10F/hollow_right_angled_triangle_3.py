n = int(input())
for i in range(n):
    if i == 0 :
        print("* "*n)
    elif i < n-1 :
        spaces = "  "*(n-i-2)
        print("* "+spaces+"* ")
    else :
        print("* ")