def writeDataToFile(TypeOfText, fileName, method):
    handle = open(fileName, method, encoding='utf-8')
    handle.write(''.join(TypeOfText) + "\n")
    handle.close()