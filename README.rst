django_dropzone
===============

This project provides a `Django`_ app ``django_dropzone`` that integrates
Django with `dropzone.js`_.

.. _Django: https://www.djangoproject.com/
.. _dropzone.js: http://www.dropzonejs.com/


Development environment setup
-----------------------------

You should use `virtualenvwrapper`_ or plain `virtualenv`_ or `venv`_ to setup
a virtual Python environment. The following examples assume virtualenvwrapper
on a Unix like system where Python 3 is available as /usr/bin/python3.

The following commands will setup a virtual environment and install the
required dependencies for the demo project and setup the django_dropzone app
for development

.. code-block:: bash

   mkvirtualenv -p /usr/bin/python3 -r requirements.txt django_dropzone
   python setup.py develop

Download and install the necessary assets for the demo project using `bower`_.

.. code-block:: bash

   bower install

Run the demo project by switching to its directory, running the Django
migrations and starting the development server.

.. code-block:: bash

   cd dropzone_demo
   python manage.py migrate
   python manage.py runserver

.. _virtualenvwrapper: https://pypi.python.org/pypi/virtualenvwrapper
.. _virtualenv: https://pypi.python.org/pypi/virtualenv
.. _venv: https://docs.python.org/3/library/venv.html
.. _bower: https://bower.io/


License
-------

django_dropzone a Django dropzone.js integration app.
Copyright (C) 2016  Jan Dittberner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

