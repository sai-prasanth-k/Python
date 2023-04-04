n = input()
first = int(n[0])
second = int(n[1])
if  int(n) % first == 0 and int(n) % second == 0 :
    print(int(n)*2)
else :
    print(int(n))