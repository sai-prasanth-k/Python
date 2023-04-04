s = input()
string = s[0:3] == "NXT"
n = s[3:]
number = int(n)
if string and (number % 2 == 0 or number % 7 == 0) :
    print("Special String")
else :
    print("Not a Special String")