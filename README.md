# Flask_SQLalchemy

Install flask_SQLAlchemy on the virtual environment.

```` # pipenv Install flask-SQLAlchemy ````

After creating ``app.py`` file.

## Create the Database

You’ll use the Flask shell to create your database.
With your virtual environment activated, set the ``app.py`` file as your Flask application using the ``FLASK_APP`` environment variable.

```` # flask shell ````

Import database object db model.

```` # from app import db ````

then run ``db.create.all()`` function to create the tables that are associated with your models.

```` # db.create.all()````

Exit shell (ctrl+D)

## Install sqlite3 

```` # sudo apt install sqlite3 ````

open ``database.db`` using sqlite3 shell

```` # sqlite3 database.db ````

Check the inserted tables usin `` .tables ``

