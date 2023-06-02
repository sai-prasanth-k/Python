scan = input()
if scan.isdigit() :
    print("Digit")
elif scan.isupper() :
    print("Uppercase Letter")
elif scan.islower() :
    print("Lowercase Letter")
else :
    print("Special Character")