from setuptools import setup

setup(
    name='tasky',
    version='0.1',
    py_modules=['main', 'task_manager', 'logger'],
    entry_points={
        'console_scripts': [
            'tasky=main:main',
        ],
    },
)
