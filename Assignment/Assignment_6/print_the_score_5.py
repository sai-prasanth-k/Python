d = int(input())
if d <= 50 :
    answer = 3 * d
elif d <= 100 :
    answer = (3 * 50) + (5 * ( d - 50))
elif d <= 200 :
    answer = (3 * 50) + (5 * 50) + (6 * (d - 100))
elif d > 200 : 
    answer = (3 * 50) + (5 * 50) + (6 * 100) + (10 * (d - 200))
    
bonus = 100 
result = 100 + answer
print(result)