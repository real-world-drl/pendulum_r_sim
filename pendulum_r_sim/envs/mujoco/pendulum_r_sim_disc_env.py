from pendulum_r_sim.envs.mujoco import PendulumRSimEnv
from gym import spaces

import numpy as np

class PendulumRSimDiscEnv(PendulumRSimEnv):
    def __init__(self):
        self.position = 0
        self.high = 2
        self.low = -2

        self.slow = 0.1
        self.fast = 0.2

        PendulumRSimEnv.__init__(self)
        # the timestamp in the pendulum_r.xml is set to 5ms and
        # the physical pendulum is optimally moving at 16Hz or with delay of 62.5ms
        self.frame_skip = 12

    def step(self, a):
        if a == 0:
            self.position -= self.fast
        elif a == 1:
            self.position -= self.slow
        elif a == 3:
            self.position += self.slow
        elif a == 4:
            self.position += self.fast

        self.position = np.clip(self.position, self.low, self.high)

        self.do_simulation(self.position, self.frame_skip)
        ob = self._get_obs()
        r = self.reward(ob)

        done = False
        return ob, r, done, {}

    def _set_action_space(self):
        bounds = self.model.actuator_ctrlrange.copy().astype(np.float32)
        self.low, self.high = bounds.T
        self.action_space = spaces.Discrete(5)
        return self.action_space
