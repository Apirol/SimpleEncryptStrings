def writeDataToFile(text, fileName):
    handle = open(fileName, 'w', encoding='utf-8')
    handle.write(''.join(text) + "\n")
    handle.close()