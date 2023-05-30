text = "I have a spare key, if I lose my key"
word_index = text.find("key")
print(word_index)


text = "coo coo"
word_index = text.find("co", 3, 6)
print(word_index)

text = "coo coo"
word_index = text.find("ha")
print(word_index)