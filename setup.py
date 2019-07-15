import setuptools

with open("README.md", "r") as fh:
    long_desc = fh.read()

setuptools.setup(
    name="fbmangler-atulin",
    version="1.0.0",
    author="Łukasz Kondracki",
    description="A tiny utility to remove Facebook tracking data from jpg images",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/Atulin/FB-Mangler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
