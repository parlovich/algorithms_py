from graph import load, Digraph


class TopologicalSort:
    def __init__(self, g: Digraph):
        self.g = g
        self.visited = [False] * self.g.v_size()
        self.post_order = []
        for v in range(self.g.v_size()):
            if not self.visited[v]:
                self._dfs(v, [])
        self.topological_order = list(reversed(self.post_order))

    def _dfs(self, v, stack):
        self.visited[v] = True
        stack.append(v)
        for i in self.g.get_adj(v):
            if not self.visited[i]:
                self._dfs(i, stack)
            else:
                if i in stack:
                    raise RuntimeError(f"Cycle is found {self._get_cycle(stack, i)}")
        self.post_order.append(v)
        stack.pop()

    def _get_cycle(self, stack, top):
        return stack[stack.index(top):]

    def get_post_order(self):
        return self.post_order

    def get_topological_order(self):
        return self.topological_order


if __name__ == "__main__":
    di_dag = load("tinyDAG.txt", Digraph)
    ts = TopologicalSort(di_dag)
    print(ts.get_post_order())
    print(ts.get_topological_order())
