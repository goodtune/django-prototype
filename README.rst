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

Features
========

- Build-in Livereload_ support.

- Possibility to provide context for Django templates.

- `Django staticfiles`_ support.

- Support for Django's `reverse resulution of named urls
  <https://docs.djangoproject.com/en/1.9/topics/http/urls/#reverse-resolution-of-urls>`_.


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

.. code-block:: yaml

  urls:
    /:
      context:
        content: It works!

And done. You can see it in browser by running::

  $ prototype

and opening http://localhost:8000/ in your browser.

While ``prototype`` command is running, you can edit you templates and changes
will be displayed automatically in the browser window.


Static files
============

All your static files should go to ``static`` directory and added to templates
using ``static`` tag:

.. code-block:: django

  {% load static %}

  <img src="{% static "img/example.png" %}" alt="just another example" />

In this example, ``img/example.png`` will be loaded from
``static/img/example.png``.


Named urls
==========

First you need to define name of your url in ``prototype.yml``:

.. code-block:: yaml

  urls:
    /my/page/:
      name: mypage

And then, you can use it in tamplates:

.. code-block:: django

    <a href="{% url 'mypage' %}">My page</a>

Now, even you change urls, they will work as long as name points to the right
url.


.. _Livereload: http://livereload.readthedocs.org
.. _Django staticfiles: https://docs.djangoproject.com/en/1.9/ref/contrib/staticfiles/
