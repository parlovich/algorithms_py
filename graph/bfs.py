from graph import load, Graph, Digraph


class BFS:
    def __init__(self, g: Graph, s: int):
        self.g = g
        self.s = s
        self.visited = [False] * g.v_size()
        self.v_from = [-1] * g.v_size()
        self.bfs(s)

    def bfs(self, v):
        q = [v]
        self.visited[v] = True
        while q:
            i = q.pop(0)
            for j in self.g.get_adj(i):
                if not self.visited[j]:
                    q.append(j)
                    self.visited[j] = True
                    self.v_from[j] = i

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
    g_bfs = BFS(g, 0)
    print(g_bfs.path_to(3))
    print(g_bfs.path_to(9))

    di_g = load("tinyDG.txt", Digraph)
    di_bfs = BFS(di_g, 8)
    print(di_bfs.path_to(12))
