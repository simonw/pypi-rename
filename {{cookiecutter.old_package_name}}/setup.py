from setuptools import setup
import os

VERSION = "{{ cookiecutter.old_package_new_version }}"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="{{ cookiecutter.old_package_name }}",
    description="{{ cookiecutter.old_package_name }} is now {{ cookiecutter.new_package_name }}",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version=VERSION,
    install_requires=["{{ cookiecutter.new_package_name }}"],
    classifiers=["Development Status :: 7 - Inactive"],
)
