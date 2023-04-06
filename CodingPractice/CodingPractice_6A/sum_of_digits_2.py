n = input()
length = len(n)

if length == 1 :
    result = int(n[0])
elif length == 2 :
    result = int(n[0]) + int(n[1])
elif length == 3 :
    result = int(n[0]) + int(n[1]) + int(n[2])
elif length == 4 :
    result = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3])
elif length == 5 :
    result = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3]) + int(n[4])
    
print(result)