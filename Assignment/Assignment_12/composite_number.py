n =int(input())
factor = 0
if n > 1 :
    factor = 0
if n < 1 :
    factor = 1
    
for i in range(2,n):
    if n % i == 0 :
        factor = factor + 1
if factor == 0 :
    print(False)
else :
    print(True)