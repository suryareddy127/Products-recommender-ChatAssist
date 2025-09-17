from setuptools import setup,find_packages
import os
import shutil

# Remove egg-info directories if they exist
for root, dirs, files in os.walk("."):
    for dir in dirs:
        if dir.endswith(".egg-info"):
            shutil.rmtree(os.path.join(root, dir))

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="products_recommender",
    version="0.1",
    author="SuryaReddy",
    packages=find_packages(),
    install_requires = requirements,
)