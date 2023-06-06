m = int(input())
n = int(input())
for i in range(m+2):
    if i == 0 or i == m+1:
        dash = "-"*n
        print("+"+dash+"+")
    else :
        hollow = " "*n
        print("|"+hollow+"|")