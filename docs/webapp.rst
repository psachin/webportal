Developer's guide
=================

Aakash School Education is developed using ``Python-Django``
framework. This provide fast development using python language as a
back-end. The frame is designed keeping in mind the collaboration of
core team(database, core engine) with design team(``HTML``, ``CSS``,
``JS``). Django is based on M(model or database)-V(views)-T(templates)
often called MVC concept.

Entire source code of this web application is hosted at
`github.com/khushbu14/webportal
<https://github.com/khushbu14/webportal>`_. To know more about setting
up **Aakash School Education** to your local GNU/Linux system, see
`ReadMe
<https://github.com/khushbu14/webportal/blob/master/ReadMe.rst>`_. To
deploy on server, see `Deploy
<https://github.com/khushbu14/webportal/blob/master/ReadMe.rst#deploy-on-server>`_.

Views
-----

Views are the basics engine of MVT. Basic redirection is written in
``views.py`` file which resides under project's app directory. Views
are python function which take user's *request* as a default
argument. It also takes care of rendering an HTML page and
redirection.

Each view(Python function) used in Aakash School Education is
described with their respective parameters below

.. automodule:: webapp.views
   :members:

Models
------

Models form a database table. Each table is defined as Python
``class`` in ``models.py`` file. In Django, database are handled using
Object Relational Mapper(ORM). Each table is treated as an object on
Django.

.. automodule:: webapp.models
   :members:


Forms
-----

User interactive form in Django is defined inside ``forms.py``
file. Each form is also defined as Python ``class``.

.. automodule:: webapp.forms
   :members:
