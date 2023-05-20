n = int(input())
string ="2"
res = 0
for i in range(1,n+1) :
    term = string * i
    res = res + int(term)
print(res)