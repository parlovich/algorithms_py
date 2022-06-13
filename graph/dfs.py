from graph import load, Graph, Digraph


class DFS:
    def __init__(self, g: Graph, s: int):
        self.g = g
        self.s = s
        self.visited = [False] * g.v_size()
        self.v_from = [-1] * g.v_size()
        self.dfs(s)

    def dfs(self, v):
        self.visited[v] = True
        for i in self.g.get_adj(v):
            if not self.visited[i]:
                self.dfs(i)
                self.v_from[i] = v

    def has_path(self, v):
        return self.visited[v]

    def path_to(self, v):
        if self.has_path(v):
            path = []
            i = v
            while i != self.s:
                path.append(i)
                i = self.v_from[i]
            path.reverse()
            return path
        return None


if __name__ == "__main__":
    g = load("tinyG.txt")
    g_dfs = DFS(g, 0)
    print(g_dfs.path_to(3))
    print(g_dfs.path_to(9))

    di_g = load("tinyDG.txt", Digraph)
    di_dfs = DFS(di_g, 8)
    print(di_dfs.path_to(12))
