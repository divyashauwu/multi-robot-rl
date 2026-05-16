import networkx as nx
import numpy as np

from environment.robot import Robot
from environment.task import Task
from environment.uncertainty import StochasticBlockages


class MultiRobotEnvironment:
    def __init__(self):
        self.graph = nx.Graph()
        self.robots = []
        self.tasks = []
        self.uncertainty_model = StochasticBlockages(0.2)

        self._build_graph()
        self._initialize_entities()

    def _build_graph(self):
        edges = [
            (0, 1, 2),
            (1, 2, 3),
            (2, 3, 2),
            (0, 3, 5),
            (1, 4, 4),
            (4, 3, 1)
        ]
        for u, v, w in edges:
            self.graph.add_edge(u, v, weight=w)

    def _initialize_entities(self):
        self.robots.append(Robot(robot_id=1, start_node=0))

        self.tasks.append(Task(task_id=1, location=2, reward=10))
        self.tasks.append(Task(task_id=2, location=4, reward=15))

    def get_state(self):
        robot_positions = [robot.current_node for robot in self.robots]

        task_states = [
            int(task.completed)
            for task in self.tasks
        ]

        return np.array(robot_positions + task_states, dtype=np.float32)

    def available_actions(self, robot: Robot):
        return list(self.graph.neighbors(robot.current_node))

    def step(self, robot: Robot, next_node: int):
        if self.uncertainty_model.is_blocked():
            reward = -5
            done = False
            return self.get_state(), reward, done

        cost = self.graph[robot.current_node][next_node]['weight']

        robot.move_to(next_node, cost)

        reward = -cost

        for task in self.tasks:
            if task.location == next_node and not task.completed:
                task.completed = True
                robot.complete_task(task.task_id)
                reward += task.reward

        done = all(task.completed for task in self.tasks)

        return self.get_state(), reward, done
