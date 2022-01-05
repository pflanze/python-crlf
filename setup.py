from setuptools import setup
import os
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="Christian Jaeger",
    author_email="copying@christianjaeger.ch",
    name="python-crlf",
    url="https://github.com/pflanze/python-crlf",
    version="cj8",
    description="Line ending detection library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['lineEnding'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ]
)
