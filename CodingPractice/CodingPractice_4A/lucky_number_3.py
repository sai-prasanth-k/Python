a = int(input())
rem2 = a % 2
rem3 = a % 3
  
is_Lucky = False
if(rem2 == 0 and rem3 == 0) :
    print("Number is divisible by 6")
    is_Lucky = True
if (rem3 == 0) and (not is_Lucky) :
    print("Number is divisible by 3")
    is_Lucky = True
if (rem2 == 0) and (not is_Lucky) :
    print("Number is divisible by 2")
    is_Lucky = True
if not is_Lucky :
    print("Number is not divisible by 2, 3 or 6")