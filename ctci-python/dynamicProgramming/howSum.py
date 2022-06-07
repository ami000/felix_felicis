from typing import List


def  how_sum(targetSum, numbers, memo = None) -> List[int] or None:
    if memo is None: memo = {}
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        remainder = targetSum - num
        remainder_result = how_sum(remainder, numbers, memo)
        if remainder_result is not None:
            memo[targetSum] =  [*remainder_result, num]
            return memo[targetSum]
    memo[targetSum] = None
    return None

# Driver code
if __name__ == '__main__':

    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(7, [2, 3]))
    print(how_sum(7, [2, 4]))
    print(how_sum(300, [7, 14]))



