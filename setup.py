import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

package_name = 'pypcl'


setuptools.setup(
    name=package_name,
    install_requires=[
        'cups==0.0.6',
        'pyserial==3.4',
    ],
    packages=setuptools.find_packages(),
    package_dir={package_name: package_name},
)
