a = int(input())
b = int(input())
count = 0
i = 1
while (i <= b):
    if i * i >= a and i * i <= b:
        count = count+1
    i = i + 1
print(count)