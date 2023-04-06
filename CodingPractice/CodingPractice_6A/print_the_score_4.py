d = int(input())
if d <= 40 :
    result = d * 2
elif d <= 60 :
    result = (2 * 40) + (4 * (d - 40))
elif d <= 120 :
    result = (2 * 40) + (4 * 20) + (6 * (d - 60))
elif d > 120 :
    result = (2 * 40) + (4 * 20) + (6 * 60) + (8 * (d - 120))
    
bonus = 50 
answer = result + bonus
print(answer)