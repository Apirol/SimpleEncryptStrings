from KeyCreation import alphabet


def encryptText(text, key):
    result = []
    for i in range(len(text)):
        result.append(key[alphabet.index(text[i])])
    return result
