from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in maintenance_gh/__init__.py
from maintenance_gh import __version__ as version

setup(
	name="maintenance_gh",
	version=version,
	description="An app used by the maintenance team of a firm to solve issues",
	author="Larry-Noble",
	author_email="nortexnoble@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
