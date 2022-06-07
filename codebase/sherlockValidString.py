def getFrequency(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


def isValid(s):
    strArray = list(s)
    freq = getFrequency(strArray)
    freqArray = list(freq.values())
    sortedFreqArray = sorted(freqArray)
    maxFreq = sortedFreqArray[len(sortedFreqArray) - 1]
    minFreq = sortedFreqArray[0]

    if maxFreq == sortedFreqArray[len(sortedFreqArray) - 2]:
        # check min Freq
        res = [i for i in sortedFreqArray if i != maxFreq]
        if len(res) > 1:
            return 'NO'
        else:
            return 'YES'
    else:
        if sortedFreqArray[len(sortedFreqArray) - 2] == minFreq:
            if maxFreq - 1 == minFreq:
                return 'YES'
        return 'NO'

if __name__ == '__main__':
    s1  = 'abcdefghhgfedecba'

    print(isValid(s1))