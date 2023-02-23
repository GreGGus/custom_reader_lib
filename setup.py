from setuptools import setup, find_packages

setup(
    name='custom_reader',
    version='1.0.3',
    url='https://github.com/mypackage.git',
    author='gregoire.portier',
    author_email='portier.gregoire@agiledss.com',
    description='Python package example',
    packages=find_packages(),    
    install_requires=['pandas >= 1.5.2','pyspark==3.1.2'],
)
