from setuptools import setup, find_packages
import subprocess
import os

def get_git_version():
    try:
        version = subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE, check=True).stdout.decode("utf-8").strip()
        if "-" in version:
            v, i, s = version.split("-")
            version = v + "+" + i + ".git." + s
        assert "-" not in version
        assert "." in version
        return version
    except subprocess.CalledProcessError:
        # Handle the case where there are no tags or the directory is not a Git repository
        return "0.0.0"

# Get the version from git tags or set a default
version = get_git_version()

# Write the version to a file
with open("VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % version)

# Read the long description from the README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wsn_sim',
    version=version,
    description='Wireless Sensor Network Simulator with AODV and DSR protocols',
    long_description=long_description,
    long_description_content_type='text/markdown',
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
