from typing import List


def  can_construct(target, wordbank, memo = None):
    if memo is None: memo = {}
    if target in memo: return memo[target]
    if target == '': return True

    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, wordbank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False
# Complexities (m = target_sum, n = len(n))

# Brute Force
# time: O(n^m * m)
# space: O(m^2)

# Memoized
# time: O(m^2 * n)
# space: O(m^2)


# Driver code
if __name__ == '__main__':

    print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    print(can_construct('eeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee',
        'eeeeee',
        'eeeeeee'
    ]))



