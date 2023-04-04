a = int(input())
b = int(input())
rem1 = a % b 
rem2 = b % a 
if rem1 < rem2 :
    print(rem1)
else :
    print(rem2)