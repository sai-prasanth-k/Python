d = int(input())
if d <= 20 :
    result = d * 2 
elif d <= 60 :
    result = (2 * 20 ) + ( 4 *(d - 20))
elif d > 60 :
    result = (2 * 20 ) + ( 4 * 40) + ( 6 *(d - 60))
    
bonus = 30
answer = bonus + result
print(answer)