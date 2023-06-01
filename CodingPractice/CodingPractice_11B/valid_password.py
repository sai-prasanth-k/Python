s = input()
contains_digit = False 
for i in s :
    digit = i.isdigit()
    if digit:
        contains_digit = True
if contains_digit :
    print("Valid Password")
else :
    print("Invalid Password")