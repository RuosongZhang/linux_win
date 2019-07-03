word = 'bananaaaaaaaaaaa'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

#new_word = upper(word)
#print(new_word)
new_word_3 = word.upper()
print(new_word_3)


index = word.find('b', 4, 8)
print(index)