def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False

    return True

def avoids(word,forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def uses_only(word,available):
    for letter in word:
        if letter not in available:
            return False

    return True

def uses_all(word,required):
    for letter in required:
        if letter not in word:
            return False
    return True

def uses_all_all(word,required):
    return uses_only(required,word)

print(has_no_e('woooooooooooed'))
print(avoids('woradddd','x'))
print(uses_only('zxcvxcv','aa'))
print(uses_all('eeersdfg','xxxee'))
print('\n')
print('\n')
print('\n')
print(uses_all_all('eeersdfg','xxxee'))