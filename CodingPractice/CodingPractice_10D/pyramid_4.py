n = int(input())
for i in range(1,n+1):
    numbers = (str(i)+" ")*i
    print(numbers)
for i in range(n):
    numbersDown = (str(n-i-1)+" ")*(n-i-1)
    print(numbersDown)