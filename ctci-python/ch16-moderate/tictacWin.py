from typing import List


def ticTacWin(moves: List[List[int]], n=3):
    a, b = [0] * 8, [0] * 8
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
        if row == 2 - col:
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

if __name__ == '__main__':
    
    mvs = [[0,0], [2, 0], [1, 1], [2, 1], [0, 2], [2, 2]]
    print(ticTacWin(mvs))