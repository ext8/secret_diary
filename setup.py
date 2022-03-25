from setuptools import setup, find_packages

setup(
    name="secret_diary",
    version="0.1.0",
    author="ext8",
    license="MIT",
    install_requires=["click"],
    packages=find_packages(),
    entry_points={"console_scripts": ["secd=app.main:main"]},
    url="https://github.com/ext8/secret_diary/",
    platforms="windows"
)
