# Unweighted graph implementation

class UnweightedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].add(vertex2)
        self.graph[vertex2].add(vertex1)

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, set())

    def __str__(self):
        result = ""
        for vertex, neighbors in self.graph.items():
            result += f"{vertex}: {neighbors}\n"
        return result

if __name__ == "__main__":
    g = UnweightedGraph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'C')
    g.add_edge('B', 'D')
    print("Graph:")
    print(g)
