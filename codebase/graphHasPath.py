graph1 = {
    'a': [ 'c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def dfHasPathI(graph, source):
    stack = [source]
    while len(stack) > 0:
        curr = stack.pop()
        # return
        print(curr)
        for neighbour in graph1[curr]:
            stack.append(neighbour)

def dfHasPathR (graph, src, dst):
    # return
    if src == dst: return True
    for neighbour in graph[src]:
        if dfHasPathR(graph, neighbour, dst):
            return True
    return False

def bfHasPathI (graph, src, dst):
    q = [src]
    while len(q) > 0:
        curr = q.pop(0)
        # return
        if curr == dst: return True
        for neighbour in graph[curr]:
            q.append(neighbour)
    return False

if __name__ == '__main__':
    # dfPrintI(graph1, 'a')
    print(dfHasPathR(graph1, 'f', 'a'))
    print(bfHasPathI(graph1, 'a', 'e'))
