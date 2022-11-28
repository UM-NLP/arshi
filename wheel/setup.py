from setuptools import setup
setup(
    name = 'persian_language',
    version='1.0',
    include_package_data=True,
    py_modules = ["persian_language"],
    packages=['.'],
    package_data={'persian_language': ['persian_language.cpython-38-x86_64-linux-gnu.so']},
    data_files=[('persian_language', ['persian_language.cpython-38-x86_64-linux-gnu.so'])],
    install_requires=['<any_python_package>==<version>']
)
