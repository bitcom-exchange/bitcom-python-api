import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitcom",
    version="0.0.4",
    author="Bit.com",
    author_email="kevin@bit.com",
    description="bitcom-python-api is a lightweight Python library for bit.com API, supporting Rest requests and "
                "event streaming using Websocket.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bitcom-exchange/bitcom-python-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
