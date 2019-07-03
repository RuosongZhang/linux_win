def find(word, letter):
    print(word)
    print(letter)
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return index

print(find('xxxxxxxxxxxxxx', 'z'))