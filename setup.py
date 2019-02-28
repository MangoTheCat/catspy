from setuptools import setup, find_packages

with open("README.md", 'r') as f:
      long_description = f.read()

setup(name='forcats',
      version='0.0.1',
      packages=find_packages(),
      description='Tools for working with categorical data',
      url='http://github.com/MangoTheCat/forcats',
      author='Mango Solutions',
      install_requires=[
            'pandas',
            'numpy'],
      license='MIT')
