from pathlib import Path
import setuptools


this_dir = Path(__file__).parent


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    with open(filename) as f:
        lineiter = (line.strip() for line in f)
        reqs = [line for line in lineiter
                if line and not line.startswith("#")]
    return reqs


with open("README.md", "r") as f:
    readme = f.read()

install_reqs = parse_requirements(str(this_dir / 'requirements.txt'))

setuptools.setup(
    name="endpoint-api-client",
    version="0.0.2",
    author="Artem Shakurov",
    author_email="galavasteg@gmail.com",
    description="This module implements API-client to storage-endpoint",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/galavasteg/api_client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=install_reqs,
)

