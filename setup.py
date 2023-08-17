from setuptools import setup, find_packages

setup(name='srealityscraper', version='0.1', packages=find_packages(exclude=["sreality", "sreality.*"]))
