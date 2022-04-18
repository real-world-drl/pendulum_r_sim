from gym.envs.registration import make, register, registry, spec
from gym.envs.registration import load_env_plugins as _load_env_plugins

# Hook to load plugins from entry points
_load_env_plugins()

register(
    id='PendulumRSim-v0',
    entry_point='pendulum_r_sim.envs.mujoco:PendulumRSimEnv',
    max_episode_steps=500,
    reward_threshold=475.0,
)

register(
    id='PendulumRSimDisc-v0',
    entry_point='pendulum_r_sim.envs.mujoco:PendulumRSimDiscEnv',
    max_episode_steps=500,
    reward_threshold=475.0,
)
