from graph import load, Edge, DiWightedGraph


class Dijkstra:

    def __init__(self, g: DiWightedGraph, s: int):
        self.g = g
        self.s = s
        self.visited = [False] * g.v_size()
        self.path_weight = [float("inf")] * g.v_size()
        self.edge_from = [-1] * g.v_size()
        self.pq = []
        self._dijkstra()

    def _relax(self, v, edge: Edge):
        if self.path_weight[v] > self.path_weight[edge.f] + edge.w:
            self.path_weight[v] = self.path_weight[edge.f] + edge.w
            self.edge_from[v] = edge.f
            # TODO replace with priority queue
            if v not in self.pq:
                self.pq.append(v)
            self.pq.sort(key=lambda x: self.path_weight[x])

    def _dijkstra(self):
        self.path_weight[self.s] = 0
        self.pq.append(self.s)
        while self.pq:
            v = self.pq.pop(0)
            self.visited[v] = True
            for w in g.get_adj(v):
                if not self.visited[w.t]:
                    self._relax(w.t, w)

    def get_path_len(self, v):
        return self.path_weight[v]

    def get_path(self, v):
        if self.edge_from[v] == -1:
            return None
        res = []
        i = v
        while i != self.s:
            res.insert(0, i)
            i = self.edge_from[i]
        return res


if __name__ == "__main__":
    g = load("tinyWDG.txt", clazz=DiWightedGraph, weighted=True)
    d = Dijkstra(g, 0)
    print(d.get_path(6))
