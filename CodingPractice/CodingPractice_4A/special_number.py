a = input()
first = a[0]
second = a[1]
suma = int(a[0]) + int(a[1]) == 7
seven = int(a[0]) == 7 or int(a[1]) == 7
div = int(a) % 7 == 0
if suma or seven or div :
    print("Special Number")
else :
    print("Normal Number")