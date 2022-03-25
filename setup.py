from setuptools import setup, find_packages

setup(
    name="secret_diary",
    version="0.1.0",
    author="ext8",
    license="MIT",
    install_requires=["Click"],
    packages=find_packages(),
    entry_points={"console_scripts": ["secd=app.main:main"]},
)
