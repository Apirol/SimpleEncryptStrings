from KeyCreation import keyCreation
from InputHandler import openFileAndReadData
from PrepareTextHandler import PrepareText
from OuputHandler import writeDataToFile
from SimpleReplacementCipher import encryptText


if __name__ == '__main__':
    keyForEssay = keyCreation()
    writeDataToFile(str(keyForEssay), 'keyForEssay.txt')
    keyForText = keyCreation()
    writeDataToFile(str(keyForText), 'keyForText.txt')
    defaultEssay = openFileAndReadData('Data/Essay.txt')
    preparedEssay = PrepareText(defaultEssay)
    defaultText = openFileAndReadData('Data/Text.txt')
    preparedText = PrepareText(defaultText)
    encryptedEssay = encryptText(preparedEssay, keyForEssay)
    encryptedText = encryptText(preparedText, keyForText)
    writeDataToFile(encryptedEssay, 'Data/encryptedEssay.txt')
    writeDataToFile(encryptedText, 'Data/encryptedText.txt')
