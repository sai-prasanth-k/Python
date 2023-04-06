percent = input()
length = len(percent) -1
a = int(percent[:length])

m = input()
if a >= 75 or m == "Y" :
    print("Allowed to write exam")
else :
    print("Cannot write exam")