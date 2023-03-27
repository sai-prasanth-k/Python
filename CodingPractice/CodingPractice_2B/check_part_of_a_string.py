word1 = input()
word2 = input()
num = int(input())
word1Len = len(word1)
word2Len = len(word2) 
result = word1[num:num + word2Len] == word2[:] and word1[num] == word2[0]

print(result)