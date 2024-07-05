# setup.py
from setuptools import setup, find_packages

setup(
    name='wsn_sim',
    version='0.1.0',
    description='Wireless Sensor Network Simulator with AODV and DSR protocols',
    author='Deepak Yadav',
    author_email='dky.united@gmail.com',
    url='https://github.com/deepak7376/wsn_sim',
    packages=find_packages(),
    install_requires=[
        'click',
        'networkx',
        'matplotlib',
        'numpy',
        'configparser'
    ],
    tests_require=[
        'unittest',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'wsn-sim=wsn_sim.cli:run_simulation',
        ],
    },
)
