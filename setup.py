import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MMShyd", #name that shows up on "pip list"
    version="0.0.1",
    author="marvin martins dos santos",
    author_email="marvin@peq.coppe.ufrj.br",
    description="MMShyd",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m4rvinm4rtins/MMShyd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
