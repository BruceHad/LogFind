# import ez_setup
# ez_setup.use_setuptools()

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'From Projects The Hard Way, this is project 1.',
    'author': 'Bruce',
    'url': 'URL to get it at.',
    'author_email': 'bahadden@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'scripts': [],
    'name': 'logfind'
}

setup(**config)