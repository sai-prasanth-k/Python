word = input()
length = len(word)
end = length - 2
start = 2
starLength = length -4
print(word[:start] + "*"*starLength + word[end:])