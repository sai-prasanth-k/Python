o = input()
a = int(input())
b = int(input())
if o == "+" :
    result = a + b
elif o == "-" :
    result = a - b
elif o == "*" :
    result = a * b
elif o == "/" :
    result = float(a / b)
elif o == "%" :
    result = a % b
    
print(result)