profession = "Doctor"
new_word = profession[:2:]
print(new_word)

bank = " ICICI "
print(bank.lower())

word = "some1" * 5
word = word[4:20:]
total = 0
for i in word :
    if i.isdigit():
        total = total + 1
print(total)


sentence = " She is capable, despite being handicapped."
sentence = sentence.replace("cap","toler")
print(sentence)

code1 = "100"
code2 = "01-01-01"
print(code1 == code1.lower())
print(code2 == code2.lower())

animal = "Rabbit" * 4
print(animal[1:9:])

palindrome = "racecar"
palindrome = palindrome.strip("r a e")
print(palindrome)

language = "Malayalam"
code = language[:9:2]
print(code)

message = "895to0i1l3Bdp4"
total = 0
for i in message :
    if i.isdigit():
        total = total + int(i)
print(total)

colour1 = "Violet"
colour2 = "Vi0l3t"
print(colour1 == colour1.upper())
print(colour2 == colour2.upper())

# string = input()
# print(len(string))

# for i in string :
#     if i.isdigit():
#         string = string.strip()
# print(string)
# print(len(string))
# string = string.upper()
# result = string.startswith("HI5")
# print(result)


fruit = " banana"
fruit = fruit.strip("a")
print(fruit)
print(len(fruit))

sentence = ".H.e.l.l.o. .w.o.r.l.d. "
sentence = sentence.strip(".")
print(sentence)

sentence = "India is a country"
is_country = sentence.endswith("Country")
print(is_country)

# code = input()
# new_code = ""
# for i in code :
#     if i.isdigit():
#         new_code = new_code + i
# print(new_code)

# name1 = input()
# name2 = name1
# name1 = name1.strip("arry")
# print(name1 == name2)

color = "*VIOLET*"
new_word = color[::3]
print(new_word)

# verb = input()
# verb = verb[3:12:4]
# count = 0
# for i in verb :
#     if i == i.upper():
#         count = count + 1
# print(count)

word = "&R&I&C&H&"
message = word[::]
print(message)

message = " bb8888bb"
message = message.strip("b")
print(message.isdigit())

country = "australia"
name1 = country.strip("a")
name2 = country.replace("a","")
print(name1 == name2)

word = input()
updated_word = word 
for i in updated_word:
    if i.isdigit():
        word = word.strip(i)
print(word)