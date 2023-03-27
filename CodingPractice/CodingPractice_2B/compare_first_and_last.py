word = input()
wordLen = len(word)
first = word[0]
last = word[wordLen-1]

result = first != last

print(result)