import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="todo.txt",
    version="0.0.1",
    author="Rakesh Singh",
    author_email="kumar.rakesh@gmail.com",
    description="Python package to manage a todo.txt style  file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rakesh.singh/todo.txt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
