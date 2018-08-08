class Graph:
    def __init__(self, E):
        self.E = E

    def __len__(self):
        return len(self.E)

    def __getitem__(self, item):
        return self.E[item]

    def keys(self):
        return self.E.keys()


class GraphIterator:
    def __init__(self, graph, start_v):
        self.graph = graph
        self.start_v = start_v
        self.visited = []
        self.queue = [start_v]

    def __iter__(self):
        return self

    def __next__(self) -> str:
        while len(self.visited) != len(self.graph):
            # case of multiple connected components
            if len(self.queue) == 0:
                not_visited = list(set(self.graph.keys()).difference(set(self.visited)))
                self.queue.append(not_visited[0])

            cur_v = self.queue.pop(0)

            if cur_v not in self.visited:
                self.visited.append(cur_v)
                self.queue.extend(self.graph[cur_v])

                return cur_v

        raise StopIteration


def test():
    E = {"A": ["B", "C"], "B": ["A", "C", "D", "E"], "C": ["A", "B", "E"], "D": ["B", "G"], "E": ["B", "C"], \
         "G": ["D"], "F": ["Q"], "Q": ["F"]}
    start_v = "A"

    graph = Graph(E)

    for v in GraphIterator(graph, start_v):
        print(v)


if __name__ == '__main__':
    test()
