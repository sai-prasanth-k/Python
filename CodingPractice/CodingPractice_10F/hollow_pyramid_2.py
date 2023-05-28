n = int(input())
for i in range(n):
    if i == 0:
        print("1 ")
    else:
        spaces = "  "*(i-1)
        number = str(i+1)+" "
        print(number+spaces+number)

for i in range(1,n):
    if i < n-1:
        numbers = str(n-i)
        spaces = " "*((2*n)-(2*i)-3)
        print(numbers+spaces+numbers)
    elif i == n-1:
        print("1 ")