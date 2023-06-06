s1 = input()
n = len(s1)
s2 = input()
res1 = ""
for i in range(n):
    if i % 2 == 0:
        res1 = res1 + s1[i]
    else :
        res1 = res1 + s2[i]
print(res1)