from setuptools import setup

package_name = 'serial_bridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nhat',
    maintainer_email='taminhnhat98@gmail.com',
    description='Serial Communication',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial = serial_bridge.main:main',
            'plotter = serial_bridge.plotter:main',
        ],
    },
)
