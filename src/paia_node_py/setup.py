from setuptools import setup

package_name = 'paia_node_py'

setup(
    name=package_name,
    version='0.0.3',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools',
        'pydantic',
        'python-dotenv'
    ],
    zip_safe=True,
    maintainer='Kylin',
    maintainer_email='kylingithubdev@gmail.com',
    description='This is a package to create a framework for development in PAIA.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publish = paia_node_py.publish:main',
            'subscribe = paia_node_py.subscribe:main',
            'service = paia_node_py.service:main',
            'client = paia_node_py.client:main',
        ],
    },
)
