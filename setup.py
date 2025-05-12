from setuptools import setup

setup(
    name="tasky",
    version="0.1",
    py_modules=["main", "db", "logger"],
    entry_points={
        "console_scripts": [
            "tasky=main:main",
        ],
    },
    extras_require={"dev": ["black", "flake8"]},
)
