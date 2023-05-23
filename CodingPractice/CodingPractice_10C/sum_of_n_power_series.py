x = int(input())
n = int(input())
sum_terms = 0
power = 1
for i in range (1,n+1) :
    term = x ** power
    power = power+ 2
    sum_terms = sum_terms + term
print(sum_terms)