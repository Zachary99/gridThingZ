import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gridThingz",
    version="1.0.0",
    author="Zephyrrus",
    author_email="zachary.ehle@gmail.com",
    description="A small package made to modify the numpy 2d data structure systed for ease of use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zachary99/gridThingZ/",
    project_urls={
        "Bug Tracker": "https://github.com/Zachary99/gridThingZ/issues/",
        "Wiki": "https://github.com/Zachary99/gridThingZ/wiki/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
