from environment.graph_environment import MultiRobotEnvironment
from planners.baseline_planner import ShortestPathPlanner
from utils.visualization import EnvironmentVisualizer


def main():
    env = MultiRobotEnvironment()

    planner = ShortestPathPlanner(env.graph)

    visualizer = EnvironmentVisualizer(env.graph)

    robot = env.robots[0]
    task = env.tasks[0]

    next_node = planner.next_step(
        robot.current_node,
        task.location
    )

    state, reward, done = env.step(robot, next_node)

    print("Next State:", state)
    print("Reward:", reward)
    print("Done:", done)

    visualizer.draw(
        robot_positions=[robot.current_node]
    )


if __name__ == "__main__":
    main()
