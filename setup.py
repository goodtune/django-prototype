from setuptools import setup, find_packages

setup(
    name="django-prototype",
    version="0.2",
    packages=find_packages(),
    author="Gary Reynolds",
    author_email="gary@touch.asn.au",
    description=(
        "Simple application to build interactive HTML based on the Django "
        "templating system."
    ),
    url="http://github.com/goodtune/django-prototype",
    test_suite="prototype.runtests.runtests",
    include_package_data=True,
    install_requires=(
        "Django>=1.9,<1.10",
        "PyYAML",
        "livereload",
        'libsass',
    ),
    entry_points={
        'console_scripts': [
            'prototype = prototype.main:main',
        ],
    },
)
