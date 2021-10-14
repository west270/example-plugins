import re

from setuptools import setup


def find_version(version_file):
    version_line = open(version_file, "rt").read()
    match_object = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_line, re.M)

    if not match_object:
        raise RuntimeError("Unable to find version string in %s" % version_file)

    return match_object.group(1)


setup(
    name="file-bytes",
    version=find_version("file_bytes/__main__.py"),
    description="Plugin that tests file uploads as bytes parameters",
    url="https://beer-garden.io",
    author="The Beergarden Team",
    author_email=" ",
    license="MIT",
    packages=["file_bytes"],
    include_package_data=True,
    install_requires=["brewtils"],
    extras_require={':python_version<"3.7"': ["importlib_resources"]},
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
