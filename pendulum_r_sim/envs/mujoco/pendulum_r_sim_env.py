import math
import pathlib

import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env


class PendulumRSimEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self):
        utils.EzPickle.__init__(self)
        xml = 'pendulum_r.xml'
        self.frame_skip = 2

        mujoco_env.MujocoEnv.__init__(self, xml, self.frame_skip)

    def step(self, a):
        self.do_simulation(a, self.frame_skip)
        ob = self._get_obs()
        r = self.reward(ob)

        done = False
        return ob, r, done, {}

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-3.01, high=3.01)
        qvel = self.init_qvel + self.np_random.uniform(size=self.model.nv, low=-2.01, high=2.01)
        self.set_state(qpos, qvel)
        return self._get_obs()

    def _get_obs(self):
        # print(self.sim.data.sensordata)
        self.sim.data.sensordata[0] = self.angle_normalize(self.sim.data.sensordata[0])
        # return np.concatenate([self.sim.data.qpos, self.sim.data.qvel]).ravel()
        return self.sim.data.sensordata

    def viewer_setup(self):
        v = self.viewer
        v.cam.trackbodyid = 0
        v.cam.distance = self.model.stat.extent

    def reward(self, observations):
        theta = np.pi - abs(observations[0])
        theta_dot = observations[1]
        return -theta ** 2 - 0.1 * theta_dot ** 2

    def angle_normalize(self, x):
        return ((x + np.pi) % (2 * np.pi)) - np.pi