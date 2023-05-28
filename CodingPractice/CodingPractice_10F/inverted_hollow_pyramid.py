n = int(input())
print("* "*n)
for i in range(1,n-1):
    spaces = " "*i
    hollow = "  "*(n-i-2)
    print(spaces+"* "+hollow+"* ")
print((" "*(n-1))+"* ")