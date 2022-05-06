from pendulum_r_sim.envs.mujoco import PendulumRSimEnv

delayed_frame_skip = 6
default_max_pre_delay = 3
default_max_post_delay = 3


class PendulumRSimPostDelayedEnv(PendulumRSimEnv):
  def __init__(self, frame_skip=delayed_frame_skip, enable_pre_delay=False, max_pre_delay=default_max_pre_delay,
               enable_post_delay=True, max_post_delay=default_max_post_delay,
               delay_in_observation=False):
    PendulumRSimEnv.__init__(self, frame_skip, enable_pre_delay, max_pre_delay,
                             enable_post_delay, max_post_delay, delay_in_observation)


class PendulumRSimPostDelaysInObs(PendulumRSimEnv):
  def __init__(self, frame_skip=delayed_frame_skip, enable_pre_delay=False, max_pre_delay=default_max_pre_delay,
               enable_post_delay=True, max_post_delay=default_max_post_delay,
               delay_in_observation=True):
    PendulumRSimEnv.__init__(self, frame_skip, enable_pre_delay, max_pre_delay,
                             enable_post_delay, max_post_delay, delay_in_observation)

class PendulumRSimShortStep(PendulumRSimEnv):
  def __init__(self, frame_skip=delayed_frame_skip, enable_pre_delay=False, max_pre_delay=default_max_pre_delay,
               enable_post_delay=False, max_post_delay=default_max_post_delay,
               delay_in_observation=False):
    PendulumRSimEnv.__init__(self, frame_skip, enable_pre_delay, max_pre_delay,
                             enable_post_delay, max_post_delay, delay_in_observation)
