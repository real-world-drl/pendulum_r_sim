from gym.envs.registration import make, register, registry, spec
from gym.envs.registration import load_env_plugins as _load_env_plugins

# Hook to load plugins from entry points
_load_env_plugins()

register(
    id='PendulumRSim-v0',
    entry_point='pendulum_r_sim.envs.mujoco:PendulumRSimEnv',
    max_episode_steps=500,
    reward_threshold=120.0,
)

register(
    id='PendulumRSimPostDelayed-v0',
    entry_point='pendulum_r_sim.envs.mujoco:PendulumRSimPostDelayedEnv',
    max_episode_steps=500,
    reward_threshold=120.0,
)

register(
    id='PendulumRSimPostDelaysInObs-v0',
    entry_point='pendulum_r_sim.envs.mujoco:PendulumRSimPostDelaysInObs',
    max_episode_steps=500,
    reward_threshold=120.0,
)

register(
    id='PendulumRSimDisc-v0',
    entry_point='pendulum_r_sim.envs.mujoco:PendulumRSimDiscEnv',
    max_episode_steps=500,
    reward_threshold=120.0,
)
