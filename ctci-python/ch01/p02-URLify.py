def URLify(s1):
    s1 = s1.strip()
    return s1.replace(' ', '%20')
if __name__ == '__main__':
    a = 'abc defgh  '
    b = 'abcdehfg'

    print(URLify(a))