from setuptools import setup

package_name = 'demo_python_pkg'

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
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            #在这里注册
            'python_node =demo_python_pkg.python_node:main',
            'learn_thread =demo_python_pkg.learn_thread:main', 
#           创建一个叫python_node的可执行文件，来源是demo_python_pkg里python_node文件里的main函数
#           记得结尾加逗号
        ],
    },
)
