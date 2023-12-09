from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
  name="zender",
  version="0.0.1",
  long_description=long_description,
  long_description_content_type="text/markdown",
  classifiers=[
    "Programming Language :: Python :: 3"
  ],
  package_dir={"": "src"},
  packages=find_packages(where="src"),
  python_requires=">=3.7, <4",
  install_requires=[
    "Jinja2",
    "click"
  ],
  entry_points={
    "console_scripts": [
      "zender=zender.cli:main"
    ]
  }
)
