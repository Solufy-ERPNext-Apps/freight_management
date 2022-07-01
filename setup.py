from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in freight_management/__init__.py
from freight_management import __version__ as version

setup(
	name="freight_management",
	version=version,
	description="This module allows you to manage all freight operations (Air, Ocean, and Land)",
	author="Solufy",
	author_email="contact@solufy.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
