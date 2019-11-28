class DJS:
    def __init__(self, nodes):
        self.parent = [-1 for i in range(nodes)]

    def find(self, index):
        if self.parent[index] == -1:
            return index
        else:
            return self.find(self.parent[index])

    def union(self, node1, node2):
        node1_p, node2_p = self.find(node1), self.find(node2)
        if node1_p == node2_p:
            return False
        else:
            self.parent[node2_p] = node1_p
            print("Parent array after performing union is {}".format(self.parent))

    def total_set(self):
        total_set = set()
        for i in range(len(self.parent)):
            parent = self.find(i)
            if parent not in total_set:
                total_set.add(parent)
        return len(total_set)


if __name__ == "__main__":
    dj_set = DJS(5)
    dj_set.union(0, 2)
    dj_set.union(0, 4)
    dj_set.union(0, 1)
    print("total num of sets in disjoint set is ", dj_set.total_set())
