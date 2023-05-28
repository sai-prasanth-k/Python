n = int(input())
for i in range(n):
    if i == 0 :
        print("# "*n)
    elif i == n -1:
        print("+ ")
    else:
        spaces = "  "*(n-i-2)
        print("+ "+spaces+"+ ")


#Another Approach

n = int(input())

first_row = "# " * n 
print(first_row)

for i in range(1, n - 1):
    middle_spaces_count = (2 * n) - (2 * (i + 1)) - 2
    middle_spaces = " " * middle_spaces_count
    row = "+ " + middle_spaces + "+ "
    print(row)

if(n > 1):
    last_row = "+"
    print(last_row)