def is_abecedarain(word):
    i = 0
    while i < len(word) - 1:
        if word[i+1] < word[i]:
            return False
        i = i+1

    return True

print(is_abecedarain('abcdefh'))