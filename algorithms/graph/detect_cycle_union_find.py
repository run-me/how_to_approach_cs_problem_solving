from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)

    def find_cycle(self):

        for parent in self.graph:
            for neighbours in self.graph[parent]:
                # if parent and neighbours have common parent

