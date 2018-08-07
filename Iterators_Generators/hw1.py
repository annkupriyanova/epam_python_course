class Graph:
    def __init__(self, E):
        self.E = E

    def __len__(self):
        return len(self.E)

    def __getitem__(self, item):
        return self.E[item]


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
            cur_v = self.queue.pop(0)

            if cur_v not in self.visited:
                self.visited.append(cur_v)
                self.queue.extend(self.graph[cur_v])

                return cur_v

        raise StopIteration


# def test():
#     E = {"A": ["B", "C"], "B": ["A", "C", "D", "E"], "C": ["A", "B", "E"], "D": ["B", "G"], "E": ["B", "C"], "G": ["D"]}
#     start_v = "A"
#
#     graph = Graph(E)
#     itr = GraphIterator(graph, start_v)
#
#     for v in itr:
#         print(v)
#
#
# if __name__ == '__main__':
#     test()