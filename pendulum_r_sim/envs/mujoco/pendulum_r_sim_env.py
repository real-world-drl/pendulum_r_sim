import math
import pathlib

import numpy as np
import gym
from gym import utils
from gym.envs.mujoco import mujoco_env


class PendulumRSimEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self, frame_skip=12, enable_pre_delay=False, max_pre_delay=3,
                 enable_post_delay=False, max_post_delay=3, delay_in_observation=False):
        utils.EzPickle.__init__(self)
        xml = pathlib.Path(__file__).parent / 'assets' / 'pendulum_r.xml'
        xml_full_path = str(xml.resolve().as_posix())

        # the timestamp in the pendulum_r.xml is set to 5ms and
        # the physical pendulum is optimally moving at 16Hz or with delay of 62.5ms
        self.frame_skip = frame_skip

        self.enable_pre_delay = enable_pre_delay
        self.enable_post_delay = enable_post_delay
        self.delay_in_observation = (enable_pre_delay or enable_post_delay) and delay_in_observation
        self.max_pre_delay = max_pre_delay
        self.max_post_delay = max_post_delay

        mujoco_env.MujocoEnv.__init__(self, xml_full_path, self.frame_skip)

        self.last_action = None


    def step(self, a):
        # this is to simulate actions arriving late (so old action is still in effect, but the pendulum is moving)
        if self.enable_pre_delay:
            pre_delay = np.random.randint(0, self.max_pre_delay)
            # pre_delay = self.np_random.normal(3, 2, 1)[0]
            if self.last_action:
                self.do_simulation(self.last_action, pre_delay)

        self.do_simulation(a, self.frame_skip)
        ob = self._get_obs()
        r = self.reward(ob)

        # this is to simulate observation arriving late (so the new action is still in effect, and the pendulum is moving)
        if self.enable_post_delay:
            post_delay = np.random.randint(0, self.max_post_delay)
            # post_delay = self.np_random.normal(6, 2, 1)[0]
            self.do_simulation(a, post_delay)
            if self.delay_in_observation:
                ob = np.append(ob, [post_delay]) # / float(self.max_post_delay)

        done = False
        return ob, r, done, {}

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-3.01, high=3.01)
        qvel = self.init_qvel + self.np_random.uniform(size=self.model.nv, low=-2.01, high=2.01)
        self.set_state(qpos, qvel)
        ob = self._get_obs()

        if self.delay_in_observation:
            # post_delay = np.random.randint(0, 3)
            # self.do_simulation(qpos, post_delay)
            # np.append(ob, [post_delay / 3.0])
            # for now don't delay reset
            ob = np.append(ob, [0])

        return ob

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

    def add_delay_to_observation_space(self):
        self.observation_space.shape
