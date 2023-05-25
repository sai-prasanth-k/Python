n = int(input())
for i in range(1,n+1):
    spaces = " "*(i-1)
    numbers = (n+1)-i
    each_numbers = str(numbers)*numbers
    row =  spaces + each_numbers
    print(row)