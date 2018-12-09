"""
Agent for learning how to control the acrobot using Gym and double
Q-Learning.

Author: Ivan A. Moreno Soto.
Last updated: 09/Dec/2018.
"""

import gym
import numpy as np

#-----------------------------

def find_range(x, interval_range):
    """
    Assigns a static number to a number x in an interval.
    """
    current_lower = -1

    while current_lower <= 1:
        if x > current_lower and x <= current_lower + interval_range:
            return current_lower + (interval_range / 2)

        current_lower += interval_range

    return x


#-----------------------------

def discretize_state(state, interval_range):
    """
    Discretizes an acrobot state using the interval_range.
    """
    return [find_range(s, interval_range) for s in state]

#-----------------------------

def choose_action(env, state, q_value_a, q_value_b, epsilon):
    """
    Chooses an action for an env in a certain state using an epsilon-greedy
    policy.
    """
    if np.random.binomial(1, epsilon) == 1:
        return env.action_space.sample()
    else:
        values_a = [q_value_a.get((str(state), a), 0) for a in range(env.action_space.n)]
        values_b = [q_value_b.get((str(state), a), 0) for a in range(env.action_space.n)]
        values_ = [a + b for a, b in zip(values_a, values_b)]

    return np.random.choice([action_ for (action_, value_) in enumerate(values_) if value_ == np.max(values_)])

#-----------------------------

env = gym.make('Acrobot-v1')
env = gym.wrappers.Monitor(env, 'acrobot_test_doubleq', force = True)

episode_count = 41001
step_size = 0.3
discount = 0.9
epsilon = 0.1
interval_range = 1.0
q_value_a = {}
q_value_b = {}

for i in range(1, episode_count+1):
    total = 0

    state = env.reset()
    state = discretize_state(state, interval_range)

    done = False

    while not done:
        action = choose_action(env, state, q_value_a, q_value_b, epsilon)
        next_state, reward, done, information = env.step(action)
        next_state = discretize_state(next_state, interval_range)
        total += reward

        # Update Q_a.
        if np.random.rand() < 0.5:
            best_a = np.argmax([q_value_a.get((str(state), a), 0) for a in range(env.action_space.n)])
            q_value_a[str(state), action] = q_value_a.get((str(state), action), 0) + step_size * (reward + discount * q_value_b.get((str(next_state), best_a), 0) - q_value_a.get((str(state), action), 0))
        # Update Q_b.
        else:
            best_a = np.argmax([q_value_b.get((str(state), a), 0) for a in range(env.action_space.n)])
            q_value_b[str(state), action] = q_value_b.get((str(state), action), 0) + step_size * (reward + discount * q_value_a.get((str(next_state), best_a), 0) - q_value_b.get((str(state), action), 0))

        state = next_state

    if total != -500:
        print("Episode {}/{}. Reward: {}.".format(i, episode_count, total))

env.env.close()

#-----------------------------
