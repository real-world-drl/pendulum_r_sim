# PendulumRSim

Simulator for a real-world implementation of a swing up pendulum using OpenAI gym interface.

Based on this real-world implementation [https://github.com/rl-sensors/pendulum-r-esp32](https://github.com/rl-sensors/pendulum-r-esp32).

## Installation

    python setup.py install

## Use

    import gym
    import pendulum_r_sim.envs

    env = gym.make('PendulumRSim-v0')
    # or for the discrete actions version
    env = gym.make('PendulumRSimDisc-v0')

    # for the versions with delays
    env = gym.make('PendulumRSimPostDelayed-v0')
    # or 
    env = gym.make('PendulumRSimPostDelaysInObs-v0')
