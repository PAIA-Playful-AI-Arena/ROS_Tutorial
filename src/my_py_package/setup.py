from setuptools import setup

package_name = 'my_py_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kylin',
    maintainer_email='kylingithubdev@gmail.com',
    description='This is my first Py package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_py_node = my_py_package.my_py_node:main'
        ],
    },
)
