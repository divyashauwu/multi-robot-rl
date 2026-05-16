from environment.graph_environment import MultiRobotEnvironment


def test_environment_initialization():
    env = MultiRobotEnvironment()

    assert len(env.robots) > 0
    assert len(env.tasks) > 0


def test_state_generation():
    env = MultiRobotEnvironment()

    state = env.get_state()

    assert state is not None
