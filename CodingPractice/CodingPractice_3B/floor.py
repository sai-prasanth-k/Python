a = input()
first = a[0]
number = int(a[1:])
if first == "R" and number < 30 :
    print("Ground Floor")
else :
    print("Not Ground Floor")