num1 = int(input())
num2 = int(input())
result = (num1 < 0 or num2 < 0) and (num1 * num2 >= -46)
print(result)