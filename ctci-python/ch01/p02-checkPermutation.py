def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

if __name__ == '__main__':
    a = 'abcdefgh'
    b = 'abcdehfg'

    print(checkPermutation(a, b))