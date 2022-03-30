from setuptools import find_packages
from setuptools import setup

setup(
    name="secret_diary",
    version="0.2.0",
    author="ext8",
    license="MIT",
    install_requires=["click", "rich", "py7zr"],
    packages=find_packages(),
    entry_points={"console_scripts": ["secd=app.main:main"]},
    url="https://github.com/ext8/secret_diary/",
    platforms="windows",
)
