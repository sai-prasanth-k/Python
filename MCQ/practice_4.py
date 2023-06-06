result = 0
for i in range(2):
    for j in range(i):
        result = result *2 
print(result)


count = 0 
for i in range (5,6):
    for i in range(5,5):
        count = count + (i+j)
print(count)

count = 0

for i in range (1,3):
    for j in range(1,3):
        if i % j == 0:
            count = count + 1

print(count)

outer = 0
inner = 0
for i in range(1,4):
    for j in range(i):
        inner = inner + 1
    outer = outer + 1

print("Outer: " + str(outer))
print("Inner: " + str(inner))