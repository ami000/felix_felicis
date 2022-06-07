from typing import List


def  count_construct(target, wordbank, memo = None):
    if memo is None: memo = {}
    if target in memo: return memo[target]
    if target == '': return 1

    total_count = 0
    for word in wordbank:
        if target.startswith(word):
            num_ways_of_rest = count_construct(target[len(word):], wordbank, memo)
            total_count += num_ways_of_rest
    memo[target] = total_count
    return total_count

# Complexities (m = target_sum, n = len(n))

# Brute Force
# time: O(n^m * m)
# space: O(m^2)

# Memoized
# time: O(m^2 * n)
# space: O(m^2)


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



