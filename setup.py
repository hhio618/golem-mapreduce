from distutils.core import setup

import setuptools

from mapreduce import VERSION

setup(
    name='golem_mapreduce',
    version=VERSION,
    description='Golem Map Reduce',
    author='hhio618',
    install_requires=["click>=7.0",
                      "appdirs",
                      "pytz",
                      "tzlocal",
                      "pyyaml>=3.13se",
                      "yapapi"],
    author_email='hhio618@gmail.com',
    url='https://github.com/hhio618/golem-mapreduce',
    keywords=['Golem', 'CI'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPLv3 License",
    ],
)
