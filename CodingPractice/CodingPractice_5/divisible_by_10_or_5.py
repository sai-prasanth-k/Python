n = int(input())
div5 = n % 5 == 0
div10 = n % 10 == 0
if div5 and div10:
    print("Divisible by 10")
elif div5 :
    print("Divisible by 5")
else :
    print("Not Divisible by 10 or 5")