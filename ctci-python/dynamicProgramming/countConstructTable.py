def  count_construct(target, wordbank):
    table = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(len(target) + 1):
        for word in wordbank:
            if i + len(word) <= len(target):
                if target[i: i + len(word)] == word:
                    table[i  + len(word)] += table[i]
    return table[len(target)]

# Complexities (m = target_sum, n = len(n))


# Driver code
if __name__ == '__main__':

    print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    print(count_construct('eeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee',
        'eeeeee',
        'eeeeeee'
    ]))

# Brute Force
# time: O(n^m * m)
# space: O(m^2)

# Memoized
# time: O(m^2 * n)
# space: O(m^2)