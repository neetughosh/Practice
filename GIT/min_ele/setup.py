import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="operation",
    version="1.0.0",
    author="Neetu",
    author_email="neetughosh17@gmail.com",
    description="Returns smallest element from an array which is strictly monotonically decreasing, the remaining elements are strictly monotonically increasing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neetughosh/Assignment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)