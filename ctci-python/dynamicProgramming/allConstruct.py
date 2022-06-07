from typing import List


def all_construct(target, wordbank, memo=None)  -> List[List[str]]:
    if memo is None: memo = {}
    if target in memo: return memo[target]
    if target == '': return [[]]

    result = []

    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            all_suffix_ways = all_construct(suffix, wordbank, memo)
            targetWays = list(map(lambda way: [word, *way], all_suffix_ways))
            result.extend(targetWays)
    memo[target] = result
    return result

# Complexities (m = target_sum, n = len(n))

# Brute Force
# time: O(n^m * m)
# space: O(m^2)

# Memoized
# time: O(m^2 * n)
# space: O(m^2)


# Driver code
if __name__ == '__main__':
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(all_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    print(all_construct('eeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee',
        'eeeeee',
        'eeeeeee'
    ]))



