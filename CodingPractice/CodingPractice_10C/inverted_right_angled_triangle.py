n = int(input())
for i in range(1,n+1):
    number = (n+1)-i
    spaces = "  "*(i-1)
    each_numbers =(str(number)+" ")*number
    row = spaces + each_numbers
    print(row)