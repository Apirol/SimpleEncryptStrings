def openFileAndReadData(fileName):
    handle = open(fileName, 'r', encoding='utf-8')
    data = handle.read()
    handle.close()
    return data