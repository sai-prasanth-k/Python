a = int(input())
b = int(input())
c = int(input())
if a == b == c :
    print("Equilateral")
elif a != b and b!= c and c != a :
    print("Scalene")
else :
    print("Isosceles")