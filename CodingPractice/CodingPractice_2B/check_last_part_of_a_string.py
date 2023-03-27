word1 = input()
word2 = input()

word2Len = len(word2) 
word1Len = len(word1) 
start = word1Len - word2Len
result = word1[start:] == word2

print(result)