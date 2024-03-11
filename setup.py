from setuptools import setup
from pathlib import Path

# Get the directory containing this file
HERE = Path(__file__).resolve().parent

# Get the long description from the README file
with open(HERE / 'README.md', encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="RR-Custom-Python-Tools",
    version="0.0.11",
    description="Frequently used python methods/libraries.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ronak Rathore",
    author_email="ronak.rathore05@gmail.com",
    license="GPLv3+",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["date_manager", "log_manager", "excel_manager"],
    include_package_data=True,
    install_requires=["pandas"]
)
