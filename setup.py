from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="forcats",
    version="0.1.0",
    packages=["forcats"],
    description="Tools for working with categorical data",
    url="http://github.com/MangoTheCat/forcats",
    author="Mango Solutions",
    zip_safe=False,
    install_requires=["pandas", "numpy"],
    license="MIT",
)
