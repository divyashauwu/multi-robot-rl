from rl.reward import MultiObjectiveReward


def test_entropy_positive():
    reward_system = MultiObjectiveReward()

    entropy = reward_system.entropy([0.5, 0.5])

    assert entropy > 0


def test_reward_computation():
    reward_system = MultiObjectiveReward()

    reward = reward_system.compute_reward(
        traversal_cost=5,
        uncertainty=2,
        tasks_completed=1,
        action_probabilities=[0.5, 0.5]
    )

    assert isinstance(reward, float)
