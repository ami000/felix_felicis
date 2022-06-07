from typing import List


def all_construct(target, wordbank)  -> List[List[str]]:
    table = [[]] * (len(target) + 1)
    table[0] = [[]]
    for i in range(len(target) + 1):
        for word in wordbank:
            if i + len(word) <= len(target) +  1:
                if target[i: i + len(word)] == word:
                    new_combinations = list(map(lambda subarray: subarray.extend, table[i]))
                    table[i + len(word)].extend(new_combinations)

    return table[len(target)]
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
    # print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    # print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    # print(all_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    # print(all_construct('eeeeeeeeeeeeeeeeeeeeeeef', [
    #     'e',
    #     'ee',
    #     'eee',
    #     'eeee',
    #     'eeeee',
    #     'eeeeee',
    #     'eeeeeee'
    # ]))



