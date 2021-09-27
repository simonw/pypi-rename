# pypi-rename cookiecutter template

Cookiecutter template for creating renamed PyPI packages

## What is this for?

If you want to rename a Python package that you have published on [PyPI](https://pypi.org/) you should follow [these steps](https://www.python.org/dev/peps/pep-0423/#how-to-rename-a-project):

* Create a renamed version of the package
* Publish it to PyPI under the new name
* Now create a final release under the old name which does the following:
  - Tells users about the name change
  - Depends on the new name, so anyone who runs `pip install oldname` will get the new name as a dependency

This cookiecutter template helps create that final release under the old name.

## Installation

You'll need to have [cookiecutter](https://cookiecutter.readthedocs.io/) installed. I recommend [pipx](https://pipxproject.github.io/pipx/) for this:

    pipx install cookiecutter

Regular `pip` will work OK too.

## Usage

Run `cookiecutter gh:simonw/pypi-rename` and then answer the prompts. Here's an example run:

    $ cookiecutter gh:simonw/pypi-rename
    new_package_name []: my-new-package-name
    old_package_name []: my-old-package-name
    old_package_new_version []: 0.2

For `old_package_new_version` you should enter a version that is higher than the most recent version that was published for the package which you are renaming.

This will create a directory called `my-old-package-name` ready to be published to PyPI.

See https://github.com/simonw/pypi-rename-demo for the output of this example.

## Publishing your renamed package to PyPI

First, publish a version of your package under the NEW name.

Now you can use the package created by this template as the last released version under the old name.

This will display a README on PyPI explaining that the module has been renamed, and will also ensure that anyone who runs `pip install my-old-package-name` will get the new package, since the new package is the only dependency for the old renamed package.

Here's an example run, including uploading the old-named package using `twine`:
```
$ cd /tmp
$ cookiecutter gh:simonw/pypi-rename
new_package_name []: datasette-insert 
old_package_name []: datasette-insert-api
old_package_new_version []: 0.5
$ cd datasette-insert-api 
$ ls
README.md	setup.py
$ python setup.py sdist
running sdist
running egg_info
creating datasette_insert_api.egg-info
writing datasette_insert_api.egg-info/PKG-INFO
...
Creating tar archive
removing 'datasette-insert-api-0.5' (and everything under it)
$ ls dist
datasette-insert-api-0.5.tar.gz
$ twine upload dist/datasette-insert-api-0.5.tar.gz
Uploading distributions to https://upload.pypi.org/legacy/
Enter your username: simonw
Enter your password: 
Uploading datasette-insert-api-0.5.tar.gz
100%|███████████████████████████████████████| 3.90k/3.90k [00:01<00:00, 3.01kB/s]

View at:
https://pypi.org/project/datasette-insert-api/0.5/
```
