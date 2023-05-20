word = input()
length = len(word)
count = 0
for i in range(length) :
    if (word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u' ):
        count = count + 1
    i=i+1
if count >=3 :
    print("String has more than two vowels")
else :
    print("String doesn't have more than two vowels")