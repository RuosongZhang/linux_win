def is_abecedarian(word):
    if len(word) <=1:
        return True

    if word[0] > word[1]:
        return False

    return is_abecedarian(word[1:])

print(is_abecedarian('abcdefghijklmo'))