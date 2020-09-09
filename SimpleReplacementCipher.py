from KeyCreation import key, alphabet


def encryptText(text):
    result = []
    for i in range (len(text)):
        result.append(key[alphabet.index(text[i])])
    return result
