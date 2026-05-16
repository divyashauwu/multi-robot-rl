import math


class MultiObjectiveReward:
    def __init__(
        self,
        alpha_cost=1.0,
        beta_uncertainty=0.5,
        gamma_task=5.0,
        lambda_entropy=0.1
    ):
        self.alpha_cost = alpha_cost
        self.beta_uncertainty = beta_uncertainty
        self.gamma_task = gamma_task
        self.lambda_entropy = lambda_entropy

    def entropy(self, probabilities):
        entropy = 0.0

        for p in probabilities:
            if p > 0:
                entropy -= p * math.log(p)

        return entropy

    def compute_reward(
        self,
        traversal_cost,
        uncertainty,
        tasks_completed,
        action_probabilities
    ):
        entropy_bonus = self.entropy(action_probabilities)

        reward = (
            -self.alpha_cost * traversal_cost
            -self.beta_uncertainty * uncertainty
            +self.gamma_task * tasks_completed
            +self.lambda_entropy * entropy_bonus
        )

        return reward
