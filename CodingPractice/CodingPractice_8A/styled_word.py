a = input()
len_of_a = len(a)
b = ""
for i in range(0, len_of_a):
    b = b + "-" + a[i]
print(b[1:])
