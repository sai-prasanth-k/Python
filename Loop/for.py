result  = 10
for i in range(1,5) :
    result = result -1
print(result)

fact = 5
for i in range(4) :
    fact = (fact * i)
print(fact)

fact = 1
for i in range(1,4) :
    fact = (fact * i)
print(fact)

num1 = 1
num2 = 15
total = 0
for i in range(num1,num2) :
    if i % 3 == 0 :
        total = total + i
print(total)

num2 = 10
total = 100
for i in range(1,num2) :
    if i % 3 == 1 :
        total = total + i
print(total)

sentence = "Solar System"
character ="s"
total = 0
for each in sentence :
    if each == character :
        total = total + 1
print(total)

book = "Alchemist"
part = ""

for i in book[6:]:
    part = part + i

print(part)

digit = 5
total = 1
for i in range(1,digit):
    if i % 3 == 0 :
        total = total * i
print(total)

x = 2
total = 0
for i in range(x):
    x = (x + 1)
    print(x)

slogan = "Save Earth, Save Lives"
length = len(slogan)
for i in range(length) :
    if slogan[i] == "" :
        print(slogan[:i])

sport = "Football"
length = len(sport)
for i in range(length) :
    print(i)

name = "Christopher"
result = ""
for i in name[:4] :
    result = result + i
print(result)

number = 10
for digit in str(number) :
    print(digit)


start = 2
end = 5
for i in range(start,end) :
    print(i * i)


number  = 234321
result = ""
for i in str(number) :
    result = result + i
print(result)

sentence = "I ate banana"
for i in range(len(sentence)):
    if sentence[i] == " ":
        print(sentence[:i])


bird = "Parrot"
for i in range(len(bird)):
    if bird[i] == "r" :
        print(bird[:i])


start = int(input())
end = int(input())
for i in range(start,end) :
    print(i)


for i in "Hardwork" :
    print(i)


quote = "Learn to explore"
total = ""
for i in quote:
    if i != " ":
        total = total + i
        
print(total)


relation = "Brother"
length = len(relation)
for i in range(length - 2) :
    print(relation[i])


number = input()
sum_of_numbers = 0
for i in number :
    sum_of_numbers = sum_of_numbers + int(i)
    
print(sum_of_numbers)


number = "45723"
total = ""
for i in range(len(number)):
    total = total + number[i]
    print(total)


verb = "Run"
result = ""
for i in range(len(verb)):
    if(i == len(verb) - 1) :
        result = result + verb[i]
    else :
        result = result + verb[i] + " "
        
print(result)


animal = "Lion"
result = ""
for i in range(len(animal)) :
    result = result + (animal[i] * i)
    
print(result)


food_item = "Rice"

for i in range(len(food_item) - 1) :
    print(i)


phone = "Samsung"
length = len(phone)
count = 0
for i in range(1,length + 1):
    count = (count * i)
    
print(count)


var1 = 1
var2 = 4
for i in range(var1, var2) :
    print(i)


