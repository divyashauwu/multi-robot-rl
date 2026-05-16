import matplotlib.pyplot as plt
import networkx as nx


class EnvironmentVisualizer:
    def __init__(self, graph):
        self.graph = graph

    def draw(self, robot_positions=None):
        pos = nx.spring_layout(self.graph)

        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_color='lightblue'
        )

        if robot_positions:
            for node in robot_positions:
                nx.draw_networkx_nodes(
                    self.graph,
                    pos,
                    nodelist=[node],
                    node_color='red'
                )

        plt.show()
