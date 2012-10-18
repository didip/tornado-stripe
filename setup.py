import os, re
from setuptools import setup, find_packages

setup(
    name = "tornado-stripe",
    version = "1.0.0",
    author = "Didip Kerabat",
    author_email = "didipk@gmail.com",
    description = ("Tornado client library for accessing Stripe API"),
    license = "Apache Software License",
    keywords = "tornado stripe api",
    url = "https://github.com/didip/tornado-stripe",
    packages=find_packages(exclude=['tests']),
    package_data = {
        # If any package contains *.txt or *.md files, include them
        '': ['*.txt', '*.md'],
    },
    include_package_data=True,
    install_requires = ["tornado>=2.4"],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
    ],
)
