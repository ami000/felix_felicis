def isUnique(s):
    charSet = set()
    for char in s:
        if charSet.__contains__(char):
            return False
        else:
            charSet.add(char)
    return True

if __name__ == '__main__':
    a = 'abcdefgh'
    b = 'aabcdeg'

    print(isUnique(a))
    print(isUnique(b))