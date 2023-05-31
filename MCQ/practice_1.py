fruit = "&W&A&T&E&R&M&E&L&O&N"
fruit_name = fruit.replace("&"," ")
fruit_name = fruit_name.lower()
print(fruit_name)

animal = "RhINoCEros"
print(animal.lower())

integer = "4 ** 5"
solution = integer.isdigit()
print(solution)

animal = "Elephant"
is_ends_with_Ant = animal.endswith("Ant")
print(is_ends_with_Ant)

word = "Container"
print(word.upper())

names = "Penny, Pin, Pack, Peak"
names = names.replace("P","J")
print(names)

profession = "Software engineer"
is_profession = profession.startswith("software")
print(is_profession)

hidden_fruit = "&b&a&n&a&n&a."
fruit = hidden_fruit[1::1]
print(fruit)

encoded_key = "*C*i*r#c#l#e*"
key = encoded_key[1::2]
print(key)