toy = input()
length = len(toy)
for i in range(1,length+1):
    print(toy[:i])

number = int(input())
pattern = " "
for i in range(0,number+1):
    pattern = str(i) + pattern

for i in range(number):
    print(pattern)

number = int(input())
factor = 0
for i in range(2,number):
    if (number % i == 0):
        factor =   factor + 1

if factor == 0 :
    print("Prime Number")
else :
    print("Not a Prime Number")


name = input()
length = len(name)
shuffle_name = ""
for i in range(length):
    index = int(input())
    shuffle_name = shuffle_name + name[index]

print(shuffle_name)


digit = int(input())
factor = 0

for i in range(2,digit):
    if (digit % i == 0):
        factor =   factor + 1

if factor == 0 :
    print("Not a Prime Number")
else :
    print("Prime Number")