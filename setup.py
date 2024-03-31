from setuptools import setup, find_packages

with open("README.md", "r") as f:
	long_description = f.read()

setup(
	name = "PyJsShift",
	version = "1.0.1",
	author = "Pairman",
	author_email = "pairmanxlr@gmail.com",
	description = "Bitwise shift with the same behavior in JavaScript.",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	license = "GNU General Public License v3 (GPLv3)",
	keywords = ["javascript", "js", "bitwise", "shift"],
	classifiers = [
		"Programming Language :: Python :: 3",
	],
	python_requires = ">= 3.0",
	url = "https://github.com/Pairman/PyJsShift",
	project_urls = {
		"Homepage": "https://github.com/Pairman/PyJsShift",
		"Changelog": "https://github.com/Pairman/PyJsShift/blob/main/CHANGELOG.md",
	},
	packages = find_packages(where = "src", include = ["pyjsshift*"]),
	package_dir = {"": "src"},
)
