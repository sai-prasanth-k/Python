a = True
while a:
    print("Python")
    a=False
print("Program")

number = 0
while number == 0:
    number = number + 1
    print(number)

a = 3
counter = 1
while counter < 2:
    a = a+1
    print(a)
    counter = counter +1
print("End")

a = 8
c = 2
sum = 0
while c < a:
    sum = ((sum + a) + c)
    a = a -1
    c = c+1
print(sum)

a = 3
b = 6
counter = 0
sum = 0
while counter < 0:
    sum = (sum + a + b)
    a = a +1
    b = b+1
    counter = counter +1
print(sum)

a = 5
while a > 0:
    print(a+1)
    a = a-1

a = 5
i = 1
while i <= a:
    if(i%2) == 0:
        print(i*i)
    i = i +1

a = 8
count = 0
while a > 0:
    a = a -1
    count = count + a
print(count)

word = "Python"
counter = 0
length = len(word)
while counter < length:
    print(word[counter])
    counter = counter + 1

a = 3
count = 0
while(a > 2) and (a<5):
    if(a%2) == 0:
        count = count + 2
        a = a +2
    else :
        count = count -1
        a = a -1
print(count)

counter = 0
condition = counter < 3
while condition:
    print(counter)
    counter = counter +1

a = 1
count = 0
while count < 3:
    a = a + 1
    print(a)
print("End")

a = True
i = 1
while a:
    if i < 3:
        a = False
    i = i + 1
print(i)

n = int(input())
count = 2
while count < 3:
    number = int(input())
    print(number)
    count = count + 1
print("End")

count = 0
word = "Hai"
result = ""
while count < 3:
    result = result + word[count]
    count = count + 1
print(result)

