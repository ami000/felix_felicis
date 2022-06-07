class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths (self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        allpaths  = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
            for p in new_paths:
                allpaths.append(p)
        return allpaths

    def get_shortest_path(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp is not None or len(sp) < len(shortest_path):
                    shortest_path = sp
        return shortest_path


def flights ():
    pass

if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Madrid'),
        ('Mumbai', 'London'),
        ('Madrid', 'London'),
        ('Madrid', 'New York'),
        ('London', 'New York'),
        ('New York', 'Toronto')
    ]

    routeGraph = Graph(routes)
    print(routeGraph.graph_dict)
    start = 'Madrid'
    end = 'New York'
    print(f'Paths between {start} and {end}:', routeGraph.get_paths(start,end))
    print(f'Shortest path between {start} and {end}:', routeGraph.get_shortest_path(start,end))