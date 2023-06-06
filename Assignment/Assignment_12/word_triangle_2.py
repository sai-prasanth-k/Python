w = input()
n = len(w)
for i in range(n):
    index = n - i
    result = w[:index]
    print(result)