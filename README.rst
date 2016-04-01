================
Django Prototype
================

.. image:: https://api.travis-ci.org/goodtune/django-prototype.png
    :alt: Build Status
    :target: https://travis-ci.org/goodtune/django-prototype

Django Prototype is a simple application which allows you to harness the power
of the `Django templating system <https://docs.djangoproject.com/en/dev/ref/templates/>`_
to produce an interactive HTML site.

The template we load is derived from the url path. For example,
http://localhost:8000/example/ will seek to load the template
``templates/example.html`` with context specified in ``prototype.yml`` file.


Quick start
===========

Install ``django-prototype``::

  $ pip install django-prototype

Create your first template at ``templates/index.html``:

.. code-block:: django
  
  <!doctype html>
  <html lang=en>
    <head>
      <meta charset=utf-8>
      <title>blah</title>
    </head>
    <body>
      <p>{{ content }}</p>
    </body>
  </html>

Create ``prototype.yml`` file:

.. code-block:: django

  urls:
    /:
      context:
        content: It works!

And done. You can see it in browser by running::

  $ prototype

and opening http://localhost:8000/ in your browser.
