n = int(input())
count = 0
for i in range(2,10) :
    if n % i == 0 :
        count = count + 1
    i = i + 1
if count > 0 :
    print("Divisible Number")
else :
    print("Indivisible Number")