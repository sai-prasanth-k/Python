s = input()
length = len(s)
contains_digit = False
for i in s :
    is_digit = i.isdigit()
    if is_digit:
        contains_digit = True
    
is_upper = s.upper() == s
is_lower = s.lower() == s
is_not_all_upper_and_lower = (not is_upper) and (not is_lower)

if is_not_all_upper_and_lower and contains_digit :
    print("Valid Password")
else :
    print("Invalid Password")