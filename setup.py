from setuptools import setup, find_packages

setup(
    name='rsnchat',
    version='2.0',
    packages=find_packages(),
    install_requires=['requests'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)