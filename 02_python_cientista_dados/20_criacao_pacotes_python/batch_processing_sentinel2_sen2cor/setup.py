from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="batch_sen2cor",
    version="0.0.3",
    author="Mateus",
    description="Batch sen2cor for sentinel2 images.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mtmiran/batch_sen2cor",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)
