import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stackx",
    version="0.0.3",
    author="Kelvin Jose",
    author_email="kelvinkonoor@gmail.com",
    description="A light-weight stack from data structures",
    long_description="In computing, a stack is a data structure used to store a collection of objects. Individual items can be added and stored in a stack using a push operation. Objects can be retrieved using a pop operation, which removes an item from the stack."
                     "For usage and more info, check https://github.com/kelvin-jose/stackX",
    long_description_content_type="text/markdown",
    url="https://github.com/kelvin-jose/stackX",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
