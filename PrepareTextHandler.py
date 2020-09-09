import re


def PrepareText(text):
    textWithoutExcessSymbols = deleteExcessSymbolsFromText(text)
    preparedText = toLower(textWithoutExcessSymbols)
    return preparedText


def toLower(text):
    return text.lower()


def deleteExcessSymbolsFromText(text):
    reg = re.compile('[^а-яА-Я]')
    updatedText = reg.sub('', text)
    return updatedText
