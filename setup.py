#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="celerydata", # Replace with your own username
    version="0.0.1",
    author="Brandon Jin",
    author_email="brandonjincmu@gmail.com",
    description="A centralized virtual data hub that contains open government data and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/greatcr7/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
