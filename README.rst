Django's built-in redirct app with some extras
============

Django's built-in redirct app with some extras.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-redirct-plus

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/arteria/django-redirct-plus.git#egg=redirct_plus

TODO: Describe further installation steps (edit / remove the examples below):

Add ``redirct_plus`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'redirct_plus',
    )

Add the ``redirct_plus`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^redirct-plus/', include('redirct_plus.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load redirct_plus_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate redirct_plus


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-redirct-plus
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
