from random import randint, random, seed

key = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') ## default key
alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
lenghtOfKey = len(key) - 1

def keyCreation ():
    for i in range(lenghtOfKey - 1):
        j = randint(0, lenghtOfKey - i)
        key[j], key[lenghtOfKey - i] = key[lenghtOfKey - i], key[j]
    return key