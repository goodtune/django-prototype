import os
import os.path

from distutils.core import setup
from string import strip

app = 'prototype'
version = "0.1"
packages = [app]
data_files = []


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


for dirpath, dirnames, filenames in os.walk(app):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        path = os.path.join(*fullsplit(dirpath)[1:])
        data_files += [os.path.join(path, f) for f in filenames]


setup(
    name='django-prototype',
    version=version,
    url='http://github.com/goodtune/django-prototype',
    author='Gary Reynolds',
    author_email='gary@touch.asn.au',
    description='Simple application to build interactive HTML based on '
        'the Django templating system.',
    install_requires=filter(None, map(strip, open('requirements.txt'))),
    packages=packages,
    package_data={app: data_files},
)
