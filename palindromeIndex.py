def palindromeIndex  (s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            newstr = s[:i] + s[i + 1:]
            print(newstr)
            if newstr[:] == newstr[::-1]:
                return i
            return -(i + 1) + len(s)
    return -1

if __name__ == '__main__':
    s1 = 'aaab'

    print(palindromeIndex(s1))