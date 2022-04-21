from pendulum_r_sim.envs.mujoco import PendulumRSimEnv


class PendulumRSimDelaysEnv(PendulumRSimEnv):
  def __init__(self, frame_skip=6, enable_pre_delay=True, enable_post_delay=True):
    PendulumRSimEnv.__init__(self, frame_skip, enable_pre_delay, enable_post_delay)