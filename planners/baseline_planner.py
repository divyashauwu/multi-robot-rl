import networkx as nx


class ShortestPathPlanner:
    def __init__(self, graph):
        self.graph = graph

    def next_step(self, current_node, target_node):
        path = nx.shortest_path(
            self.graph,
            source=current_node,
            target=target_node,
            weight='weight'
        )

        return path[1]
