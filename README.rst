================
Django Prototype
================

.. image:: https://api.travis-ci.org/goodtune/django-prototype.png
    :alt: Build Status
    :target: https://travis-ci.org/goodtune/django-prototype

Django Prototype is a simple application which allows you to harness the power
of the `Django templating system <https://docs.djangoproject.com/en/dev/ref/templates/>`_
to produce an interactive HTML site.

The template we load is derived from the path on the Django site. For example,
starting up the development server and accessing http://localhost:8000/example/
will seek to load the template ``prototype/example/index.html`` with an empty
context.

