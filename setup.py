import itertools
import os.path
import sys

from setuptools import find_packages, setup

# Don't import module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "pendulum_r_sim"))
from version import VERSION

# Environment-specific dependencies.
extras = {
    "mujoco": ["mujoco-py<2.2,>=2.1"],
    "other": [],
}

# Meta dependency groups.
all_groups = set(extras.keys())

extras["all"] = list(
    itertools.chain.from_iterable(map(lambda group: extras[group], all_groups))
)

setup(
    name="pendulum_r_sim",
    version=VERSION,
    description="PendulumRSim: Simulator for a real-world implementation of a swing up pendulum using OpenAI gym interface",
    url="https://github.com/real-world-drl/pendulum_r_sim/",
    author="Peter Bohm",
    author_email="p.bohm@uq.edu.au",
    license="MIT",
    packages=[package for package in find_packages() if package.startswith("pendulum_r_sim")],
    zip_safe=False,
    install_requires=[
        "numpy>=1.18.0",
        "cloudpickle>=1.2.0",
        "importlib_metadata>=4.10.0; python_version < '3.10'",
        "gym>=0.23.1",
    ],
    extras_require=extras,
    package_data={
        "pendulum_r_sim": [
            "envs/mujoco/assets/*.xml",
            "py.typed",
        ]
    },
    tests_require=["pytest", "mock"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)