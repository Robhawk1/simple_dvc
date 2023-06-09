
from setuptools import setup, find_packages

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = "src",
    version = "0.0.1",
    author = "Robhawk1",description = "A small package for dvc ml pipeline demo",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/Robhawk1/simple_dvc",
    author_email="robhawk97@gmail.com",
    #package_dir={"":"src"},
    #packages=find_packages(where="src"),License="GNU",
    packages = ["src"],
    python_requires=">=3.6",
    install_requires=[
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',
        'scikit-learn'
    ]
)
