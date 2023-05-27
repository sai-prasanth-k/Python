n = int(input())
for i in range(n):
    if i == 0 :
        print("* ")
    elif i == n -1:
        print("* "*n)
    else :
        spaces = "  "*(i-1)
        print("* "+spaces+"* ")