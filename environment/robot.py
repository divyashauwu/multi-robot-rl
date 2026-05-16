class Robot:
    def __init__(self, robot_id: int, start_node: int):
        self.robot_id = robot_id
        self.current_node = start_node
        self.total_cost = 0.0
        self.completed_tasks = []

    def move_to(self, node: int, cost: float):
        self.current_node = node
        self.total_cost += cost

    def complete_task(self, task_id: int):
        self.completed_tasks.append(task_id)
