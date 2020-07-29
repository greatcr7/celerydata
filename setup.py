#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="celerydata", # project name
    version="0.0.1",
    author="Brandon Jin",
    author_email="brandonjincmu@gmail.com",
    description="A centralized virtual data hub that contains open government data and more.",
    long_description=long_description, # README
    long_description_content_type="text/markdown", # file type of README
    url="https://github.com/greatcr7/", # package website
    packages=setuptools.find_packages(include=['celerydata']), # packages and subpackages created in this project
    package_data={
    'sample': ['package_data.dat'],
    }, # data file needed for the project
    install_requires=['requests'], # required external packages needed for this project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Data Scientists, Business Analysts and Developers",
    ],
    keywords='centralized opensource datahub',
    package_dir={'': 'celerydata'},
    python_requires='>=3', # required Python version
)
