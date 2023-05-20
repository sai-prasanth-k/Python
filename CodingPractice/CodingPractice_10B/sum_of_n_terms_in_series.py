x=(input())
n= int(input())
res= 0
for i in range(1,n+1) :
    term = x * i
    res = res + int(term) 
print(res)