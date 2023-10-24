from collections import defaultdict

class Q:
    def __init__(self, alpha=0.5, gamma=0.5):
        self.alpha = alpha
        self.gamma = gamma
        self.values = defaultdict(lambda: defaultdict(lambda: 0.0))

    def update(self, state, action, next_state, reward):
        value = self.values[state][action]
        v = list(self.values[next_state].values())
        next_q = max(v) if v else 0
        value = value + self.alpha * (reward + self.gamma * next_q - value)
        self.values[state][action] = value

    def get_best_action(self, state):
        keys = list(self.values[state].keys())
        if not keys:
            return None
        return max(keys, key=lambda x: self.values[state][x])
