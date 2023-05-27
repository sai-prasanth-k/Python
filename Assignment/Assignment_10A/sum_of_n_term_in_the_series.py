x = int(input())
n = int(input())
power = 1
sumOfTerm = 0
for i in range(0,n):
    if i % 2 == 0:
        terms = x ** power
        sumOfTerm = sumOfTerm + terms
    else :
        terms = -1*(x **power)
        sumOfTerm = sumOfTerm + terms
    power = power + 2
print(sumOfTerm)