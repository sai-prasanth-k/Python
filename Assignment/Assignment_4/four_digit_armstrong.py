n = input()
first = int(n[0])
second = int(n[1])
third = int(n[2])
fourth = int(n[3])
result = first ** 4 + second ** 4 + third ** 4 + fourth ** 4 == int(n)
if result:
    print("Armstrong Number")
else :
    print("Not an Armstrong Number")