import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='ROS2 learning package',
    license='MIT',
    extras_require={'test': ['pytest']},
    entry_points={
        'console_scripts': [
            'talker = my_robot.talker:main',
            'listener = my_robot.listener:main',
            'service_server = my_robot.service_server:main',
            'service_client = my_robot.service_client:main',
            'param_node = my_robot.param_node:main',
            'sensor_publisher = my_robot.sensor_publisher:main',
        ],
    },
)
