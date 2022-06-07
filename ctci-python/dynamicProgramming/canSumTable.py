def can_sumT (target_sum, numbers):
    table = [False] * (target_sum + 1)
    table[0] = True
    for i in range(target_sum + 1):
        if table[i]:
            for num in numbers:
               if i + num <= target_sum: table[i + num] = True
    return table[target_sum]

if __name__ == '__main__':
    print(can_sumT(7, [2, 3]))
    print(can_sumT(7, [5, 3, 4, 7]))
    print(can_sumT(7, [2, 4]))
    print(can_sumT(8, [2, 3, 5]))
    print(can_sumT(300, [7, 14]))