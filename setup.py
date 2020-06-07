import setuptools
from lightdiscord import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lightdiscord",  # Replace with your own username
    version=__version__,
    author="Th0rgal",
    author_email="thomas.marchand@tuta.io",
    description="A small pythonic alternative to discord.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.io/lightdiscord",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # DBAD license is not supported :'(
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
