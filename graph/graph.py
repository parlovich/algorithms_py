
class Graph:
    def __init__(self, n_v):
        self.n_v = n_v
        self.adj = [None] * n_v
        for i in range(n_v):
            self.adj[i] = []

    def v_size(self):
        return self.n_v

    def add_edge(self, i, j):
        self.adj[i].append(j)
        self.adj[j].append(i)

    def get_adj(self, i):
        return self.adj[i]


class Digraph(Graph):
    def add_edge(self, i, j):
        self.adj[i].append(j)


class Edge:
    def __init__(self, f: int, t: int, weight: float):
        self.f = f
        self.t = t
        self.w = weight


class WeightedGraph:
    def __init__(self, n_v: int):
        self.n_v = n_v
        self.adj = [None] * n_v
        for i in range(n_v):
            self.adj[i] = []

    def v_size(self):
        return self.n_v

    def add_edge(self, edge: Edge):
        self.adj[edge.f].append(edge)
        self.adj[edge.t].append(edge)

    def get_adj(self, i):
        return self.adj[i]


class DiWightedGraph(WeightedGraph):

    def add_edge(self, edge: Edge):
        self.adj[edge.f].append(edge)


def load(file, clazz=Graph, weighted=False):
    with open(file, "r") as f:
        n_v = int(f.readline())
        n_e = int(f.readline())
        g = clazz(n_v)
        for i in range(n_e):
            edge = f.readline().split(" ")
            if weighted:
                g.add_edge(Edge(int(edge[0]), int(edge[1]), float(edge[2])))
            else:
                g.add_edge(int(edge[0]), int(edge[1]))
    return g


if __name__ == "__main__":
    g = load("tinyG.txt")
    d = load("tinyG.txt", Digraph)
    print(d)

