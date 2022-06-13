from graph import load, Graph, Digraph
from topological_sort import get_postorder


class ConnectedComponents:
    def __init__(self, g: Graph):
        self.g = g
        self.marked = [-1] * g.v_size()
        self.count = 0

        for v in range(g.v_size()):
            if self.marked[v] == -1:
                self._dfs(v)
                self.count += 1

        self.components = [[] for i in range(self.count)]
        for i in range(g.v_size()):
            self.components[self.marked[i]].append(i)

    def _dfs(self, v):
        self.marked[v] = self.count
        for i in self.g.get_adj(v):
            if self.marked[i] == -1:
                self._dfs(i)

    def get_count(self):
        return self.count

    def is_connected(self, i, j):
        return self.marked[i] == self.marked[j]

    def get_components(self):
        return self.components


class StrongComponents:
    def __init__(self, g: Digraph):
        self.g = g

    def is_strongly_connected(self, i, j):
        pass


if __name__ == "__main__":
    g = load("tinyG.txt")
    c = ConnectedComponents(g)
    print(c.get_components())
