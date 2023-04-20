n = int(input())
first = int(input())
greatest = first

for i in range(n - 1):
    m = int(input())
    if m > greatest:
        greatest = m

print(greatest)