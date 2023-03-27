word1 = input()
word2 = input()

last1 = len(word1) -3
last2 = len(word2) -3

result = word1[last1:] == word2[last2:]

print(result)