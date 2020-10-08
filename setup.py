import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="file-traverser-abeahm", # Replace with your own username
    version="0.1.0",
    author="Alex Beahm",
    author_email="alexanderbeahm@gmail.com",
    description="Simple injectible rescursive file system processor.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexanderBeahm/file-traverser.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)