
def tic_tac_win_3x3(moves):
    a, b = [0] * 8, [0] * 8 # <---- can be changed to 2n + 2 for nxn
    for i in range(len(moves)):
        row, col = moves[i]
        if i % 2 == 0:
            player = a
        else:
            player = b
        player[row] += 1
        player[col + 3] +=1
        if row == col:
            player[6] +=1
        if row == 2 - col: # <---- can change 2 to n - 1 for nxn
            player[7]
    for i in range(len(a)):
        if a[i] == 3:
            return 'A'
        elif b[i] == 3:
            return 'B'
    if len(moves) == 9:
        return 'Draw'
    else:
        return 'Pending'


def test_tic_tac_win():
    test_cases = [
        [[[0, 0], [2, 0], [1, 1], [2, 1], [0, 2], [2, 2]], 'A'],
        [[[0, 1], [1, 1], [0, 2], [0, 0], [1, 2], [2, 2]], 'B'],
        [[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]], 'Draw'],
        [[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1]], 'Pending']
    ]
    for mvs, expected in test_cases:
        assert tic_tac_win_3x3(mvs) == expected

if __name__ == '__main__':
    test_tic_tac_win()