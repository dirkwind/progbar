
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="progbar",
    version="0.0.1",
    author="Harry Heitmeier",
    author_email="dirkwind707@gmail.com",
    description="A simple progress bar.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/dirkwind/progbar/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)