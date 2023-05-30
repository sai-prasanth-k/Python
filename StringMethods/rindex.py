text = "I have a spare key, if I lose my key"
word_index = text.rindex("key")
print(word_index)


text = "coo coo coo"
word_index = text.rindex("co", 3, 10)
print(word_index)


text = "coo coo"
word_index = text.rindex("ha")
print(word_index)