word = input()
n = input()
n = int(n)
length = len(word)
last3 = length-3
print((word[last3:])*n)