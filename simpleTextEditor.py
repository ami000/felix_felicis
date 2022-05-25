# Enter your code here. Read input from STDIN. Print output to STDOUT

def textEdit(ops):
    s = ''
    historyStack = []
    for op in ops:
        op = op.split()
        if op[0] == '1':
            s += op[1]
            historyStack.append(s)
        elif op[0] == '2':
            s = s[:-int(op[1]) or '']
            historyStack.append(s)
        elif op[0] == '3':
            print(s[int(op[1]) - 1])
        else:
            historyStack.pop()
            if len(historyStack) == 0:
                s = ''
            elif len(historyStack) == 1:
                s = historyStack[0]
            else:
                s = historyStack[-1]


if __name__ == "__main__":
    # n = int(input())
    ops1 = ['1 abc', '3 3', '2 3', '1 xy', '3 2', '4', '4', '3 1']
    # for i in range(len(ops1)):
    #     ops1.append(input())

    textEdit(ops1)