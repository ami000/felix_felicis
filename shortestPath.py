reached = set()
paths = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['v', 'w']
]

def buildGraph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    q = [(nodeA, 0)]
    visited = {nodeA}
    while len(q) > 0:
        currNode, distance = q.pop(0)
        if currNode == nodeB: return distance
        for neighbour in graph[currNode]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append((neighbour, distance + 1))
    return -1

if __name__ == '__main__':
    print(shortestPath(paths, 'w', 'z'))