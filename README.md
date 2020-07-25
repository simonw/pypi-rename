# pypi-rename cookiecutter template

Cookiecutter template for creating renamed PyPI packages

## Installation

You'll need to have [cookiecutter](https://cookiecutter.readthedocs.io/) installed. I recommend pipx for this:

    pipx install cookiecutter

Regular `pip` will work OK too.

## Usage

Run `cookiecutter gh:simonw/pypi-rename` and then answer the prompts. Here's an example run:

    $ cookiecutter gh:simonw/pypi-rename
    new_package_name []: my-old-package-name
    old_package_name []: my-new-package-name
    old_package_new_version []: 0.2

For `old_package_new_version` you should enter a version that is higher than the most recent version that was published for the package which you are renaming.

This will create a directory called `my-old-package-name` ready to be published to PyPI.

See https://github.com/simonw/pypi-rename-demo for the output of this example.

## Publishing your renamed package to PyPI

First, publish a version of your package under the NEW name.

Now you can use the package created by this template as the last released version under the old name.

This will show a README explaining that the module has been renamed, and will also ensure that anyone who runs `pip install my-old-package-name` will get the new package, since the new package is the only dependency for the old renamed package.
