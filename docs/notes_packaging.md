# Python Packaging

## Notes

[1](https://the-hitchhikers-guide-to-packaging.readthedocs.org/en/latest/creation.html)
[2](https://packaging.python.org/en/latest/installing.html)
[3](https://pythonhosted.org/setuptools/setuptools.html)

## Structure

Generally a package will be structured like:

MyPackage/
    bin/
    docs/
    README.txt
    setup.py
    mypackage/
        __init__.py
        my.py
        package.py
    tests/
        __init__.py
        test_location.py
        test_utils.py

The setup.py file will look something like:

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    config = {
        'author': 'Author Name',
        'description': 'Package description.',
        'url': 'URL to get it at.',
        'author_email': 'bahadden@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['logfind'],
        'scripts': [],
        'name': 'mypackage'
    }

    setup(**config)

Running the command to create the distribution:

    python setup.py sdist

Creates a 'dist' directory that contains a tar.gz file for distribution.

