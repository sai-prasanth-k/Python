n = int(input())

left_spaces = " " * 2 * (n - 1)
first_row = left_spaces + "*"
print(first_row)

for i in range(1, n - 1):
    left_spaces = " " * 2 * (n - i - 1)
    middle_spaces = " " * (2 * (i) - 1)
    row = left_spaces + "*" + middle_spaces + "*"
    print(row)
    
last_row = "* " * n
print(last_row)


# Another Approach

n = int(input())
spaces = "  "*(n-1)
print(spaces+"* ")
for i in range(1,n-1):
    spaces = "  "*(n-i-1)
    hollowSpaces = "  "*(i-1)
    print(spaces+"* "+hollowSpaces+"* ")
print("* "*n)