import copy
import random
from collections import deque, namedtuple
import torch.nn as nn
import torch.nn.functional as F
import torch

Transition = namedtuple('Transition',
                        ('state', 'action', 'next_state', 'reward'))


class ReplayMemory(object):

    def __init__(self, capacity):
        self.memory = deque([], maxlen=capacity)

    def push(self, *args):
        """Save a transition"""
        self.memory.append(Transition(*args))

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)


class CNNModel(nn.Module):
    def __init__(self, n_channel, n_action):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=n_channel,
                               out_channels=32, kernel_size=8, stride=4)
        self.conv2 = nn.Conv2d(32, 64, 4, stride=2)
        self.conv3 = nn.Conv2d(64, 64, 3, stride=1)
        self.fc = torch.nn.Linear(7 * 7 * 64, 512)
        self.out = torch.nn.Linear(512, n_action)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc(x))
        output = self.out(x)
        return output


class DQN:
    def __init__(self, n_channel, n_action, lr=0.05):
        self.criterion = torch.nn.MSELoss()
        self.model = CNNModel(n_channel, n_action)
        self.model_target = copy.deepcopy(self.model)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr)


def replay(self, memory, replay_size, gamma):

    """
    Воспроизведение опыта с целевой сетью
    @param estimator: буфер воспроизведения опыта
    @param replay_size: сколько примеров использовать при каждом
              обновлении модели
    @param gamma: коэффициент обесценивания
    """
    if len(memory) >= replay_size:
        replay_data = random.sample(memory, replay_size)
        states = []
        td_targets = []
        for state, action, next_state, reward, is_done in replay_data:
            states.append(state.tolist()[0])
            q_values = self.predict(state).tolist()[0]
            if is_done:
                q_values[action] = reward
            else:
                q_values_next = self.target_predict(next_state).detach()
                q_values[action] = reward + gamma * torch.max(q_values_next).item()
            td_targets.append(q_values)
    self.update(states, td_targets)
