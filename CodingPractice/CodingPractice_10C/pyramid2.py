n = int(input())
for i in range(n):
    spaces = "  "*(n-i-1)
    number = (str(i+1)+" ")*((2*i)+1)
    row = spaces + number
    print(row)