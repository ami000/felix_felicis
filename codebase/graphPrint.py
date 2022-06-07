graph1 = {
    'a': [ 'c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def dfPrintI(graph, source):
    stack = [source]
    while len(stack) > 0:
        curr = stack.pop()
        # return
        print(curr)
        for neighbour in graph[curr]:
            stack.append(neighbour)

def dfPrintR (graph, source):
    # return
    print(source)
    for neighbour in graph[source]:
        dfPrintR(graph, neighbour)

def bfPrintI (graph, source):
    q = [source]
    while len(q) > 0:
        curr = q.pop(0)
        # return
        print(curr)
        for neighbour in graph[curr]:
            q.append(neighbour)


if __name__ == '__main__':
    # dfPrintI(graph1, 'a')
    # dfPrintR(graph1, 'a')
    bfPrintI(graph1, 'a')
