from setuptools import find_packages, setup

with open('README.md') as f:
  long_description = f.read()

setup(
    name='ai-api-plugin',
    version='2024.9.21',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url='',
    author='Thomas Kottke',
    author_email='t.kottke90@gmail.com',
    packages=find_packages(),
    python_requires=">=3.11.9",
    install_requires=[
      'pluggy==1.5.0'
    ],
    extra_require={
      "dev": {}
    }
)