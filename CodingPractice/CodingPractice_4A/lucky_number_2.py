n = input()
first = int(n[0])
second = int(n[1])
if (first == 9 or second == 9) or int(n) % 9 == 0 :
    print("Lucky Number")
else :
    print("Unlucky Number")