import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CakeBaking", # Replace with your own username
    version="0.0.3",
    author="Kiran Wijesooriya",
    author_email="kiranw1000@gmail.com",
    description="Package meant to be used for beginners learning with the cake baking analogy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kiranw1000/BakingACake/archive/0.0.3.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
          'time',
      ],
)