def how_sumT (target_sum, numbers):
    table = [None] *  (target_sum + 1)
    table[0] = []
    for i in range(target_sum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target_sum:
                    table[i + num] = [*table[i], num]
    return table[target_sum]

if __name__ == '__main__':
    print(how_sumT(7, [2, 3]))
    print(how_sumT(7, [5, 3, 4, 7]))
    print(how_sumT(7, [2, 4]))
    print(how_sumT(8, [2, 3, 5]))
    print(how_sumT(300, [7, 14]))