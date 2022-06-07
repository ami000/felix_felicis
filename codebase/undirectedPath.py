paths = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

def undirectedPathDFR ( edges, nodeA, nodeB):
    graph =  buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, set())

def hasPath (graph, src, dst, visited: set):
    if src in visited: return False
    visited.add(src)
    if src == dst: return True
    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dst, visited):
            return True
    return False


def buildGraph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

if __name__ == '__main__':
    # dfPrintI(graph1, 'a')
    print(undirectedPathDFR(paths, 'i', 'k'))