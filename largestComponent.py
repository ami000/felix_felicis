reached = set()
graph1 = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


def largestComponent(graph):
    largest = 0
    for node in graph:
        size = exploreSize(graph, node, reached)
        if size > largest: largest = size
    return largest

def exploreSize(graph, curr, visited:set):
    if curr in visited: return 0
    visited.add(curr)
    size = 1
    for neighbour in graph[curr]:
        size += exploreSize(graph, neighbour, visited)
    return size

if __name__ == '__main__':
    print(largestComponent(graph1))