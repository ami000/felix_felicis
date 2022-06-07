def  can_constructT(target, wordbank) -> bool:
    table = [False] * (len(target)  + 1)
    table[0] = True

    for i in range(len(target)  + 1):
        if table[i]:
            for word in wordbank:
                if target[i : i + len(word)] == word:
                    if i + len(word) <= len(target):
                        table[i + len(word)] = True
    return table[len(target)]

# Driver code
if __name__ == '__main__':

    print(can_constructT('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(can_constructT('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(can_constructT('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    print(can_constructT('eeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee',
        'eeeeee',
        'eeeeeee'
    ]))

# Complexities (m = target_sum, n = len(n))

# Brute Force
# time: O(n^m * m)
# space: O(m^2)

# Tabulation
# time: O(m^2 * n)
# space: O(m)


