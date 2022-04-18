# PendulumRSim

Simulator for a real-world implementation of a swing up pendulum using OpenAI gym interface.

## Installation

    python setup.py install

## Use

    import gym
    import pendulum_r_sim.envs

    env = gym.make('PendulumRSim-v0')
    # or for the discrete actions version
    env = gym.make('PendulumRSimDisc-v0')
