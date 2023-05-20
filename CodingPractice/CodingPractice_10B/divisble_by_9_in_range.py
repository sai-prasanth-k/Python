m = int(input())
n = int(input())
string = ""
count = 0
for i in range (m,n+1):
    if i % 9 == 0 :
        string = string + str(i)+" "
        count = count +1
    i = i +1
if count > 0 :
    print(string)
else :
    print("No Numbers found")