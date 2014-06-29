=========
Webportal
=========

A **Webportal** to provide education material to the students.

(Summer Internship 2014, Indian Institute of Technology, Bombay)

Clone
-----

- Make sure your Internet is working.
- Clone this repo by typing ::

    git clone https://github.com/khushbu14/webportal.git


Installation
------------

- Install Virtual Environment using the following command ::

    sudo apt-get install python-virtualenv

- Create a Virtual Environment ::

    virtualenv /path/to/virtualenv

- Activate the virtualenv using the command ::

    source /path/to/virtualenv-name/bin/activate

- Change the directory to the `webportal/` project using the command ::

    cd /path/to/webportal

- Install pre-requisites using the command ::

    pip install -r requirements.txt

  or you can also type ::

    easy_install `cat requirements.txt`


Usage
-----

- Using sqlite3 (For local server only). We recommend to use `MySQL` for
  server. See `settings.py` file for usage.

  Open `webportal/webportal/settings.py` file and do the following changes ::

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backend.sqlite3',
        'NAME'  : 'webportal.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
    }


- Initialize the database using the command ::

    cd /path/to/webportal
    python manage.py syncdb

- Start the server using the command ::

    python manage.py runserver

Deploy on server
----------------
(Tested on Ubuntu 12.04)

- Make sure your Internet is working.
- Clone this repo by typing ::

    git clone https://github.com/khushbu14/webportal.git

- Collect static files(Required by Django's admin interface) ::

    cd webportal
    python manage.py collectstatic

- Install *virtualenv* using above steps and mention the path in
  `wsgi.py` file.

  Assuming the virtualenv `wb_virt` in placed inside `/var/www/` directory

  ------8<------------------------------------------------------------------------

  ::

    import os
    import sys

    # We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
    # if running multiple sites in the same mod_wsgi process. To fix this, use
    # mod_wsgi daemon mode with each site in its own daemon process, or use
    # os.environ["DJANGO_SETTINGS_MODULE"] = "webportal.settings"

    activate_this = '/var/www/wb-virt/bin/activate_this.py'
    execfile(activate_this, dict(__file__=activate_this))
    sys.path.append("/var/www/webportal/") # Project directory PATH.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webportal.settings")

    # This application object is used by any WSGI server configured to use this
    # file. This includes Django's development server, if the WSGI_APPLICATION
    # setting points here.
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

    # Apply WSGI middleware here.
    # from helloworld.wsgi import HelloWorldApplication
    # application = HelloWorldApplication(application)

  ------------------------------------------------------------------------>8------

- Make sure you have following dependencies installed on server ::

    sudo apt-get install apache2
    sudo apt-get install python-dev
    sudo apt-get install libmysqlclient-dev
    sudo apt-get install libapache2-mod-wsgi

- Configure apache2 conf file: `/etc/apache2/httpd.conf`

  Assuming the project is inside: `/var/www/`

  ------8<------------------------------------------------------------------------

  ::

     Alias /media/ /var/www/webportal/media/
     Alias /static/ /var/www/webportal/webportal/static/

     <Directory /var/www/webportal/static>
     Require all granted
     </Directory>

     <Directory /var/www/webportal/media>
     Require all granted
     </Directory>

     WSGIScriptAlias / /var/www/webportal/webportal/wsgi.py
     WSGIPythonPath /var/www/webportal

     <Directory /var/www/webportal/webportal/wsgi.py>
     <Files wsgi.py>
     Require all granted
     </Files>
     </Directory>

  ------------------------------------------------------------------------>8------

- Finally restart apache server ::

    sudo service apache2 restart


Documentation
-------------

To generate docs:

- Make sure you have Python `Sphinx` installed(See `requirements.txt`
  file)

- Change to `docs/` directory ::

    cd docs

- Export `DJANGO_SETTINGS_MODULE` ::

    export DJANGO_SETTINGS_MODULE=webportal.settings

- Generate HTML ::

    make html

  and browse `docs/_build/html/index.html` file from Web Browser

- Generate PDF(Optional)

  Make sure you have `latex` installed. ::

    make latexpdf

  PDF file will be generated inside `docs/_build/latex` directory.

Contributing
------------

- Never edit the master branch.
- Make a branch specific to the feature you wish to contribute on.
- Send us a pull request.
- Please follow `PEP8 <http://legacy.python.org/dev/peps/pep-0008/>`_
  style guide when coding in Python.

License
-------

GNU GPL Version 3, 29 June 2007.

Please refer this `link <http://www.gnu.org/licenses/gpl-3.0.txt>`_
for detailed description.
