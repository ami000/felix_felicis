from typing import List


def  best_sum(target_sum, numbers, memo = None) -> List[int] or None:
    if memo is None: memo = {}
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers, memo)
        if remainder_combination is not None:
            combination = [*remainder_combination, num]
            # if the combination < shortest_combination: update
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    memo[target_sum] = shortest_combination
    return memo[target_sum]

# Complexities (m = target_sum, n = len(n))

# Brute Force
# time: O(n^m * m)
# space: O(m^2)

# Memoized
# time: O(m^2 * n)
# space: O(m^2)


# Driver code
if __name__ == '__main__':

    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(8, [1, 4, 5]))
    print(best_sum(100, [1, 2, 5, 25]))



