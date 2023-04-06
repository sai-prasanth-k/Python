n1 = int(input())
n2 = int(input())
if n1 < 0 and n2 < 0 :
    n1 = n1 * (-1)
    n2 = n2 * (-1)
    if n1 - n2 > 0 :
        print(n1 - n2)
    else :
        print((n1 - n2) *(-1))
elif n1 < 0 and n2 > 0 :
    n1 = n1 * (-1)
    print(n1 + n2)
elif n1 > 0 and n2 < 0 :
    n2 = n2 * (-1)
    print(n1 + n2)
elif n1 > 0 and n2 > 0 :
    if n1 - n2 > 0 :
        print(n1 - n2)
    else :
        print((n1 - n2) *(-1))