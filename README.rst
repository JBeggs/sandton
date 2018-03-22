Santon Website
==============
**Santon Website & Product Catalog**

.. contents:: Contents
    :depth: 5
    
.. _http://localhost:8000/: http://localhost:8000/

Dependencies
------------

* Python 2.7
* Django 1.10
* Django Colorfield 0.1.10
* Gunicorn 19.6.0 (optional but recommended)
* Pillow 3.3.1

Installation
------------

Run the following commands in your terminal::
    
    $ git clone git@github.com:qoda/santon.git
    $ cd santon/
    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.pip
    $ ./manage.py migrate
    $ ./manage.py runserver
    
Go to `http://localhost:8000/`_ to view the site on the development server.
