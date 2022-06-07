def palindromeP(s):
    s = sorted(s.replace(' ', ''))
    stack = []
    for i in range(len(s)):
        if s[i] in stack:
            stack.remove(s[i].lower())
        else:
            stack.append(s[i].lower())
    print(stack)
    return len(stack) <= 1

if __name__ == '__main__':
    a = 'aabb'
    print(palindromeP(a))