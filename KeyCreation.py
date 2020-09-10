from random import randint


alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
lenghtOfKey = len(alphabet) - 1


def keyCreation():
    key = list(alphabet)
    for i in range(lenghtOfKey - 1):
        j = randint(0, lenghtOfKey - i)
        key[j], key[lenghtOfKey - i] = key[lenghtOfKey - i], key[j]
    return key
