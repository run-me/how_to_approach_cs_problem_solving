"""
A simple 05_graph representation which does the following operations
0. Initialize the 05_graph
1. Add nodes to the 05_graph
2. Add edges between one node to other
3. Get nodes in the 05_graph
4. Get edges for nodes in the 05_graph
"""


class Graph:

    def __init__(self, num_nodes):
        """
        0. Initialize a list with number of nodes
        1. Initialize the adjacency matrix for the 05_graph with the provided number of nodes
        2.
        """
        self.num_nodes = num_nodes
        self.adj_matrix = [[None for col in range(len(num_nodes))] for row in range(len(num_nodes))]
        self.node_list = [0]*num_nodes

