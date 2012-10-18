import os, re
from setuptools import setup


def parse_requirements(file_name):
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            # TODO support version numbers
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'\s*-f\s+', line):
            pass
        else:
            requirements.append(line)

    return requirements


setup(
    name = "tornado-stripe",
    version = "1.0.0",
    author = "Didip Kerabat",
    author_email = "didipk@gmail.com",
    description = ("Tornado client library for accessing Stripe API"),
    license = "Apache Software License",
    keywords = "tornado stripe api",
    url = "https://github.com/didip/tornado-stripe",
    install_requires = parse_requirements('requirements.txt'),
    packages=['tornado_stripe'],
    long_description=open('README.md').read(),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
    ],
)
