"""
A simple graph representation which does the following operations
0. Initialize the graph
1. Add nodes to the graph
2. Add edges between one node to other
3. Get nodes in the graph
4. Get edges for nodes in the graph
"""


class Graph:

    def __init__(self, num_nodes):
        """
        0. Initialize a list with number of nodes
        1. Initialize the adjacency matrix for the graph with the provided number of nodes
        2.
        """
        self.num_nodes = num_nodes
        self.adj_matrix = [[None for col in range(len(num_nodes))] for row in range(len(num_nodes))]
        self.node_list = [0]*num_nodes

