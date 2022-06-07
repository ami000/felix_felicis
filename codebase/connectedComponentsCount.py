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


def connectedComponents(graph):
    count = 0
    for node in graph:
        print(reached)
        if explore(graph, node, reached):
            count  += 1
    return count

def explore(graph, curr, visited:set):
    if curr in visited: return False
    visited.add(curr)
    for neighbour in graph[curr]:
        explore(graph, neighbour, visited)
    return True

if __name__ == '__main__':
    print(connectedComponents(graph1))