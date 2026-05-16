from dataclasses import dataclass


@dataclass
class Task:
    task_id: int
    location: int
    reward: float
    completed: bool = False
