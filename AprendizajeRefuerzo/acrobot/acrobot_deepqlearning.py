"""
Agent for learning how to control the acrobot using Gym and deep
Q-Learning.

Author: Ivan A. Moreno Soto.
Last updated: 09/Dec/2018.
"""

import keras
import gym
import numpy as np
import random
from collections import deque

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

#---------------------------------------------------------

def build_model(agent):
    """
    Builds a neural network to approximate the action-value of the agent.
    """
    # NN for the q-function.
    model = Sequential()
    model.add(Dense(24, input_dim = agent.state_size, activation = 'linear'))
    # Hidden layer.
    model.add(Dense(24, activation = 'relu'))
    # Output layer.
    model.add(Dense(agent.action_size, activation = 'linear'))
    # Compile the model.
    model.compile(loss = 'mse', optimizer = Adam(lr = agent.learning_rate))
    return model

def remember(agent, state, action, reward, next_state, done):
    """
    Appends the transition to the agent's memory.
    """
    agent.memory.append((state, action, reward, next_state, done))

def act(agent, state):
    """
    Decides the action for a given state with an epsilon-greedy policy.
    """
    if np.random.rand() <= agent.epsilon:
        return random.randrange(agent.action_size)

    act_values = agent.model.predict(state)
    return np.argmax(act_values[0])

def replay(agent, batch_size):
    """
    Trains the neural network through the repetition of past iterations.
    """
    minibatch = random.sample(agent.memory, min(batch_size, len(agent.memory)))

    # Training the neural network through minibatches.
    for (state, action, reward, next_state, done) in minibatch:
        target = reward
        if done:
            target = reward
        else:
            target = reward + agent.gamma * np.amax(agent.model.predict(next_state)[0])

        target_f = agent.model.predict(state)
        target_f[0][action] = target
        agent.model.fit(state, target_f, epochs=1, verbose=0)

#---------------------------------------------------------

class DQLAgent:
    """
    An agent that learns through the use of a neural network.
    """

    def __init__(self, state_size, action_size):
        """
        Creates the agent with the specified parameters.
        """
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.9
        self.epsilon = 0.1
        self.learning_rate = 0.08
        self.model = build_model(self)

#---------------------------------------------------------

env = gym.make("Acrobot-v1")
env = gym.wrappers.Monitor(env, 'acrobot_deepq_test', force = True)

state_size = env.observation_space.shape[0]
action_size = env.action_space.n
acrobot_agent = DQLAgent(state_size, action_size)
acrobot_agent.model.load_weights('./acrobot_weights/acrobot-dqnproper_3_200.h5')

batch_size = 50
num_episodes = 200

for e in range(num_episodes):
    state = env.reset()

    done = False
    state = np.reshape(state, (1, state_size))

    total = 0

    while not done:
        action = act(acrobot_agent, state)
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, (1, state_size))

        total += reward

        remember(acrobot_agent, state, action, reward, next_state, done)
        state = next_state

        replay(acrobot_agent, batch_size)

    print("Episode {}/{}. Score: {}.".format(e, num_episodes, total))

    if e % 50 == 0:
        acrobot_agent.model.save_weights('./acrobot_weights/acrobot-dqnproper_4_' + str(e) + '.h5')

env.env.close()
acrobot_agent.model.save_weights('./acrobot-dqnproper_4_200.h5')

#---------------------------------------------------------
