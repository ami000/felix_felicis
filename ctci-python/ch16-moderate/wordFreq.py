def wordFreq(book, target):
    bookFreqDict = {}
    for word in book:
        if word in bookFreqDict:
            bookFreqDict[word] += 1
        else:
            bookFreqDict[word] = 1
    return bookFreqDict[target]


if __name__ == '__main__':
    book1 = ['abc', 'abc', 'e']
    book2 = []
    book3 = ['abc']

    word1 = 'abc'
    word2 = 'e'
    word3 = 'meta'

    print(wordFreq(book2, word1))