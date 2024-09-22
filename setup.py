import json
from setuptools import find_packages, setup

with open('README.md') as f:
  long_description = f.read()

with open('pi-package.json') as pkg:
  packageFields = json.loads(pkg.read())

setup(
    **packageFields,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url='',
    author='Thomas Kottke',
    author_email='t.kottke90@gmail.com',
    package_dir={'': 'lib'},
    packages=find_packages(where='lib'),
    python_requires=">=3.11.9",
    install_requires=[
      'pluggy==1.5.0'
    ],
    extra_require={
      "dev": {}
    }
)