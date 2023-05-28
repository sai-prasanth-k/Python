n = int(input())
for i in range(n):
    spaces = " "*(n-i-1)
    if i == 0:
        print(spaces+"* ")
    elif i == n -1 :
        print("* "*n)
    else:
        hollowSpaces = "  "*(i-1)
        print(spaces+"* "+hollowSpaces+"* ")