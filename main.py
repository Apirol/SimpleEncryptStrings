from KeyCreation import keyCreation, key
from InputHandler import openFileAndReadData
from PrepareTextHandler import PrepareText
from OuputHandler import  writeDataToFile
from SimpleReplacementCipher import encryptText



if __name__ == '__main__':
    keyForEsse = keyCreation()
    writeDataToFile(str(key), 'key.txt', 'w')
    keyForText = keyCreation()
    writeDataToFile(str(key), 'key.txt', 'a')
    defaultEsse = openFileAndReadData('Data/esse.txt')
    preparedEsse = PrepareText(defaultEsse)
    defaultText = openFileAndReadData('Data/text.txt')
    preparedText = PrepareText(defaultText)
    encryptedEsse = encryptText(preparedEsse)
    encryptedText = encryptText(preparedText)
    writeDataToFile(encryptedEsse, 'Data/encryptedEsse.txt', 'w')
    writeDataToFile(encryptedText, 'Data/encryptedText.txt', 'w')
