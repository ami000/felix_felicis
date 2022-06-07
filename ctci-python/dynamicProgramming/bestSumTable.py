def best_sumT (target_sum, numbers):
    table = [None] *  (target_sum + 1)
    table[0] = []
    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target_sum:
                    if not table[i + num] or len(table[i + num]) > len([*table[i], num]):
                        table[i + num] = [*table[i], num]

    return table[target_sum]

if __name__ == '__main__':
    print(best_sumT(7, [5, 3, 4, 7]))
    print(best_sumT(8, [2, 3, 5]))
    print(best_sumT(8, [1, 4, 5]))
    print(best_sumT(7, [2, 4]))
    print(best_sumT(100, [1, 2, 5, 25]))