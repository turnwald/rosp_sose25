from setuptools import find_packages, setup

package_name = 'mobrob_simplebot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='turnwald',
    maintainer_email='alen.turnwald@thi.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simplebot_sim = mobrob_simplebot.simplebot_sim:main',
            'simplebot_control = mobrob_simplebot.simplebot_control:main',
            'simplebot_control_p = mobrob_simplebot.simplebot_control_param:main',
            'simplebot_control_ps = mobrob_simplebot.simplebot_control_param_srv:main',
            'turtlesim_pose_converter = mobrob_simplebot.turtlesim_pose_converter:main'
        ],
    },
)
