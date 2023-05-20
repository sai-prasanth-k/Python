m = int(input())
n = int(input())
count = 0
number = ""
for i in range(m,n+1):
    if i % 6 == 0:
        count = count + 1
        number = number + str(i) + " "
        
if count == 0:
    print("No Numbers Found")
else :
    print(number)