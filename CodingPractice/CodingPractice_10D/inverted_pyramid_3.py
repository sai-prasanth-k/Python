# simple Approach
n = int(input())
print("+ "*n)
for i in range(n):
    stars = "* "*(n-i-1)
    spaces = " "*(i+1)
    print(spaces+stars)

# Using If-else Condition
n = int(input())
for i in range(n):
    if i == 0:
        spaces = " "*i
        pluses = "+ "*(n-i)
        result = spaces+pluses
    else:
        stars = "* "*(n-i)
        spaces = " "*(i)
        result = spaces+stars
    print(result)