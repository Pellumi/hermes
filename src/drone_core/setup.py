from setuptools import setup
import os
from glob import glob

package_name = 'drone_core'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='User',
    maintainer_email='user@example.com',
    description='Core logic for Hermes drone',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'telemetry_node = drone_core.telemetry_node:main',
            'path_planner_node = drone_core.path_planner_node:main',
            'controller_node = drone_core.controller_node:main',
        ],
    },
)
