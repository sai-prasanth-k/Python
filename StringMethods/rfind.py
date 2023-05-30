text = "I have a spare key, if I lose my key"
word_index = text.rfind("key")
print(word_index)


text = "coo coo coo"
word_index = text.rfind("co", 3, 10)
print(word_index)


text = "coo coo"
word_index = text.rfind("ha")
print(word_index)