from setuptools import setup, find_packages
setup(
    name = 'persian_language',
    version='1.0',
    packages=find_packages(include=['persian', 'persian.*']),
    install_requires=['<any-python-package>==<vrsion>']

                      )
