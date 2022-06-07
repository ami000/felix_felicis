def  can_sum(targetSum, numbers, memo = {}) -> bool :
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False
    for num in numbers:
        remainder = targetSum - num
        if can_sum(remainder, numbers, memo):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


# Driver code
if __name__ == '__main__':

    t1, n1 = 7, [5, 3, 4, 7]
    print(can_sum(t1, n1))

    t2, n2, = 8, [3, 9]

    t3, n3 = 300, [7, 14]
    print(can_sum(t3, n3))



