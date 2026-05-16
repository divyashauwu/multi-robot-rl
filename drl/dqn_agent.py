import random

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim


class QNetwork(nn.Module):
    def __init__(self, state_size, action_size):
        super().__init__()

        self.layers = nn.Sequential(
            nn.Linear(state_size, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, action_size)
        )

    def forward(self, x):
        return self.layers(x)


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        self.gamma = 0.99
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01

        self.model = QNetwork(state_size, action_size)

        self.optimizer = optim.Adam(
            self.model.parameters(),
            lr=1e-3
        )

        self.loss_fn = nn.MSELoss()

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.action_size - 1)

        with torch.no_grad():
            state_tensor = torch.FloatTensor(state)
            q_values = self.model(state_tensor)

        return torch.argmax(q_values).item()
