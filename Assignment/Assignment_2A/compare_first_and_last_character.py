word= input()
num = int(input())
length = len(word)
last = length - num
result = word[:num] != word[last:]

print(result)