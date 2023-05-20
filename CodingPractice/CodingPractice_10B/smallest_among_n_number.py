n = int(input())
first_letter = int(input())
smallest = first_letter
for i in range(n-1):
    m = int(input())
    if m < smallest :
        smallest = m;
    i = i + 1
print(smallest)
    